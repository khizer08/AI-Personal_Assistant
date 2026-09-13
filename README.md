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

## Running the App

1. Create and activate a virtual environment if needed.
2. Install dependencies:

```bash
pip install flask
```

3. Start the Flask development server:

```bash
python main.py
```

4. Open the app in your browser at:

```text
http://127.0.0.1:5000/
```

## Notes

This project is a starter implementation for a personal assistant interface. You can extend the backend and frontend to add chat, task management, note-taking, scheduling, and AI-powered responses.
