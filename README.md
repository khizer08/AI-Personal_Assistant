# AI Personal Assistant

A lightweight Flask-based personal assistant web app that generates an interactive UI for asking questions, tracking tasks, and exploring notes.

## Project Structure

```text
main.py              # Flask application entry point
static/
    app.js            # Frontend JavaScript behavior
    style.css        # Styling for the UI
templates/
    index.html       # Main page template
```

## Features

- Simple web UI for an AI-style personal assistant
- Flask backend serving the homepage
- Static assets for styling and UI behavior
- HTML template-based front page
- Gemini-powered `/ask` and `/summarize` endpoints

## Local Development

1. Create and activate a virtual environment if needed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the environment variable `GEMINI_API_KEY` in a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

4. Start the Flask development server:

```bash
python main.py
```

5. Open the app in your browser at:

```text
http://127.0.0.1:5000/
```

## Deployment on Render

This app is ready for a Render Web Service using the Flask app entrypoint in `main.py`.

Recommended Render settings:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn main:app`
- Environment Variables: add `GEMINI_API_KEY`

A health check route is available at `/health`.

## Notes

This project is a starter implementation for a personal assistant interface. You can extend the backend and frontend to add chat, task management, note-taking, scheduling, and AI-powered responses.
