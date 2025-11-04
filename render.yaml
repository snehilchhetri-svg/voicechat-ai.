services:
  - type: web
    name: jarvis-ai
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn main:app
    envVars:
      - key: GROQ_API_KEY
        sync: false
