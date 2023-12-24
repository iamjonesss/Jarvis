from dotenv import load_dotenv
import openai as gpt
import speech_recognition as sr
import pyttsx3 as tsx
import os

gpt_key = gpt.api_key = os.getenv("API_KEY")
jarvis = tsx.init()
audio = sr.Recognizer()



# jarvis.say('Olá, como posso ajudar?')
# jarvis.runAndWait()