from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Jarvis Cloud Brain is running!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get("query", "").lower()

    # Simple demo logic — later we can plug in GPT or logic functions
    responses = [
        "I'm here, sir. What would you like me to do?",
        "At your service, sir.",
        "Processing your command.",
        "Of course, I’ll handle that immediately."
    ]

    if "time" in user_input:
        from datetime import datetime
        return jsonify({"response": f"The time is {datetime.now().strftime('%I:%M %p')}"})
    elif "how are you" in user_input:
        return jsonify({"response": "I'm fully operational and ready to assist you, sir."})
    else:
        return jsonify({"response": random.choice(responses)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
