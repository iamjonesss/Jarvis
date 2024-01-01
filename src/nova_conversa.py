from config_geral import gpt_key
from openai import OpenAI
import requests
import json

def nova_conversa(mensagem):
    client = OpenAI(api_key=gpt_key)
    
    resposta_user = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": 'user', "content": mensagem}
        ]
    )
    return resposta_user['choices'][0]["menssage"]