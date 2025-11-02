from flask import Flask, request, jsonify
import speech_recognition as sr
from gtts import gTTS
import os

app = Flask(__name__)

recognizer = sr.Recognizer()

# 🎤 Function to take voice input
def listen_command():
    try:
        with sr.Microphone() as source:
            print("🎙 Listening for command...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("🔍 Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
    except sr.WaitTimeoutError:
        return "Listening timed out."
    except sr.UnknownValueError:
        return "Sorry, I didn’t catch that."
    except Exception as e:
        return str(e)

# 🗣 Convert text to speech
def speak(text):
    print(f"💬 Jarvis: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")

@app.route("/")
def home():
    return "🚀 Jarvis Voice Assistant is running!"

@app.route("/voice", methods=["GET"])
def voice():
    command = listen_command()
    response = f"You said: {command}"
    speak(response)
    return jsonify({"command": command, "response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
