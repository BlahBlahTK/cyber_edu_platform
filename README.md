# CyberGuard Educational Platform

An interactive cybersecurity education platform built with Python (Flask) and JavaScript. Learn about common web vulnerabilities like SQL Injection, XSS, and Phishing, and use our AI-powered assistant to analyze potential threats.

## Features

- **Educational Modules**: deep dives into SQL Injection, Cross-Site Scripting (XSS), and Phishing.
- **AI Security Assistant**: A chatbot that helps users identify potential attacks based on descriptions (powered by OpenAI or compatible LLMs).
- **Modern UI**: A responsive, dark-themed design for an immersive learning experience.

## Prerequisites

- Python 3.8+
- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd cyber_edu_platform
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: You may need to create a `requirements.txt` first with `pip freeze > requirements.txt` if not provided, or simply run `pip install flask openai python-dotenv`)*

4. **Configuration:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - (Optional) Add your OpenAI API key to `.env` to enable the full AI chatbot. If left blank, the bot runs in demo mode.

## Running the Application

1. **Start the Flask server:**
   ```bash
   flask run --port=8080
   ```
   *Note: We use port 8080 because port 5000 is often reserved by macOS system services (AirPlay).*

2. **Open your browser:**
   Navigate to [http://localhost:8080](http://localhost:8080)

## Project Structure

- `app.py`: Main Flask application.
- `templates/`: HTML templates.
- `static/`: CSS and JavaScript files.
   - `style.css`: Custom styling.
   - `chat.js`: Frontend logic for the chatbot.

## License

MIT License
