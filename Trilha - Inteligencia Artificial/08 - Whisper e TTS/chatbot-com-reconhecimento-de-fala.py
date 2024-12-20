import speech_recognition as sr
from io import BytesIO
from pygame import mixer
from pathlib import Path

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

recognizer = sr.Recognizer()

ARQUIVO_AUDIO = 'audios/fala_assistant.mp3'

def grava_audio():
    with sr.Microphone() as source:
        print('Ouvindo...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    return audio

def transcricao_audio(audio):
    wav_data = BytesIO(audio.get_wav_data())
    wav_data.name = 'audio.wav'
    transcricao = client.audio.transcriptions.create(
        model='whisper-1',
        file=wav_data,
        language='pt'
    )
    return transcricao.text

def completa_texto(mensagens):
    resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-3.5-turbo-0125',
    max_tokens=1000,
    temperature=0
    )
    return resposta

def cria_audio(texto):
    mixer.quit()
    if Path(ARQUIVO_AUDIO).exists():
        Path(ARQUIVO_AUDIO).unlink()
    resposta = client.audio.speech.create(
        model='tts-1',
        voice='onyx',
        input=texto
    )
    resposta.write_to_file(ARQUIVO_AUDIO)
    
def roda_audio():
    mixer.init()
    mixer.music.load(ARQUIVO_AUDIO)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.quit()

if __name__ == '__main__':
    mensagens = []
    
    while True:
        audio = grava_audio()
        transcricao = transcricao_audio(audio)
        
        mensagens.append({'role': 'user', 'content': transcricao})
        print(f'User: {mensagens[-1]['content']}')
        
        resposta = completa_texto(mensagens)
        mensagens.append({'role':'assistant', 'content': resposta.choices[0].message.content})
        print(f'Assistant: {mensagens[-1]['content']}')
        
        cria_audio(mensagens[-1]['content'])
        roda_audio()
