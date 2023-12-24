from config_geral import gpt_key, jarvis, audio
import speech_recognition as sr
import pyttsx3 as tsx

try:
    
    with sr.Microphone() as source:
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        
        
except Exception as e:
    print(f'Erro na aplicação: {e}')