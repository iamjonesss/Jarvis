import openai as gpt
import speech_recognition as sr
import pyttsx3 as tsx

gpt_key = gpt.api_key = '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'
jarvis = tsx.init()
audio = sr.Recognizer()



# jarvis.say('Olá, como posso ajudar?')
# jarvis.runAndWait()