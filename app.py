import gradio as gr
import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def voice_ai(audio):
    try:
        with sr.AudioFile(audio) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            reply = f"You said: {text}"
            engine.save_to_file(reply, "reply.mp3")
            engine.runAndWait()
            return reply, "reply.mp3"
    except Exception as e:
        return str(e), None

gr.Interface(
    fn=voice_ai,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=["text", "audio"],
    title="Voice AI Assistant"
).launch()
