from flask import Flask, request, jsonify
import os, requests

app = Flask(__name__)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------- Brain 1 : LLaMA 3 (main) ----------
def ask_brain_1(prompt):
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions",
                      headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

# ---------- Brain 2 : Mixtral (backup) ----------
def ask_brain_2(prompt):
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions",
                      headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

# ---------- Jarvis main logic ----------
def jarvis(prompt):
    ans = ask_brain_1(prompt)
    unsure_signs = ["not sure", "don't know", "uncertain", "maybe", "perhaps"]
    if any(x in ans.lower() for x in unsure_signs):
        backup = ask_brain_2(prompt)
        return f"[Brain 1 unsure]\n{backup}"
    return ans

# ---------- Flask route ----------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    return jsonify({"reply": jarvis(prompt)})

@app.route("/")
def home():
    return "Jarvis v1 — Ready to Serve ⚡"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
