import os

from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from google import genai
from google.genai import types


app = Flask(__name__)

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

client = None
if api_key:
    client = genai.Client(api_key=api_key)
else:
    app.logger.warning("GEMINI_API_KEY is not set in the environment. Configure it before using /ask and /summarize.")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/ask", methods=["POST"])
def ask():
    if client is None:
        return jsonify({"error": "GEMINI_API_KEY is not configured"}), 500

    question = request.form.get("question")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction="Act like a helpful personal assistant.",
            temperature=0.7,
            max_output_tokens=512
        )
    )

    answer = response.text.strip()

    return jsonify({"response": answer}), 200


@app.route("/summarize", methods=["POST"])
def summarize():
    if client is None:
        return jsonify({"error": "GEMINI_API_KEY is not configured"}), 500

    email_text = request.form.get("email")

    if not email_text:
        return jsonify({"error": "Email text is required"}), 400

    prompt = f"""
    Summarize the following email in 2-3 sentences.

    Email:
    {email_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="Act like an expert email assistant.",
            temperature=0.3,
            max_output_tokens=512
        )
    )

    summary = response.text.strip()

    return jsonify({"response": summary}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)