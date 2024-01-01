from config_geral import gpt_key, jarvis, audio
from src.comando import comando
from src.nova_conversa import nova_conversa
import speech_recognition as sr
import pyttsx3 as tsx


try:
    texto = comando()
    nova_conversa(texto)
    
    
except Exception as e:
    print(f'Erro na aplicação: {e}')