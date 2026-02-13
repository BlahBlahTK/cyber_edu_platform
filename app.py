from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)

# Configure OpenAI/LLM client
api_key = os.getenv("OPENAI_API_KEY")
client = None
if api_key:
    client = openai.OpenAI(api_key=api_key)

# Mock data for attacks
ATTACKS = {
    "sql-injection": {
        "title": "SQL Injection (SQLi)",
        "description": "SQL Injection is a code injection technique where an attacker executes malicious SQL statements that control a web application's database server.",
        "how_it_happens": "It happens when user input is not properly sanitized or validated before being used in an SQL query. For example, if a login form takes a username without checking for special characters, an attacker can input SQL commands.",
        "prevention": "Use parameterized queries (prepared statements) instead of string concatenation. Validate and sanitize all user inputs. Use an ORM (Object-Relational Mapping) framework.",
        "severity": "High"
    },
    "xss": {
        "title": "Cross-Site Scripting (XSS)",
        "description": "XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users.",
        "how_it_happens": "It occurs when an application includes untrusted data in a new web page without proper validation or escaping. If a website displays a user comment without cleaning it, a script tag in the comment will execute in everyone's browser.",
        "prevention": "Escape untrusted data based on the output context (HTML, JavaScript, CSS). Use Content Security Policy (CSP). Sanitize input using libraries designed for it.",
        "severity": "Medium to High"
    },
    "phishing": {
        "title": "Phishing",
        "description": "Phishing is a type of social engineering where an attacker sends a fraudulent message designed to trick a person into revealing sensitive information.",
        "how_it_happens": "Attackers send emails or create websites that look legitimate (like a bank login page) to steal credentials. They often use urgency or fear to manipulate victims.",
        "prevention": "Verify the sender's email address. Check URLs carefully before clicking. Enable Multi-Factor Authentication (MFA). Educate users to recognize suspicious messages.",
        "severity": "High"
    }
}

@app.route('/')
def index():
    return render_template('index.html', attacks=ATTACKS)

@app.route('/attack/<attack_id>')
def attack_detail(attack_id):
    attack = ATTACKS.get(attack_id)
    if not attack:
        return "Attack not found", 404
    return render_template('attack.html', attack=attack)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat_api():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    system_prompt = """You are a cybersecurity expert assistant. 
    Your goal is to help users identify potential cyber attacks based on their descriptions.
    Analyze their situation and suggest if it sounds like SQL Injection, XSS, Phishing, or another common attack.
    Explain why and suggest immediate steps they should take.
    Keep your language simple and educational.
    If you are unsure, advise them to contact a professional security team.
    """

    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", # Or compatible model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            bot_reply = response.choices[0].message.content
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        # Mock response if no API key is set
        bot_reply = "I am currently in demo mode (no API key configured). Based on your description, this sounds like it might be a Phishing attempt given the suspicious email context. (Please configure OPENAI_API_KEY to get real AI analysis)."

    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
