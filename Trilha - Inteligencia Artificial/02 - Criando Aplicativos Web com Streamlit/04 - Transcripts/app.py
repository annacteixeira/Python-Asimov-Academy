import streamlit as st
import openai
import queue
import time
from moviepy import VideoFileClip
from pathlib import Path
from streamlit_webrtc import WebRtcMode, webrtc_streamer

from dotenv import find_dotenv, load_dotenv
_= load_dotenv(find_dotenv())

client = openai.Client()

PASTA_TEMP = Path(__file__).parent / 'temp'
PASTA_TEMP.mkdir(exist_ok=True)
ARQUIVO_AUDIO_TEMP = PASTA_TEMP / 'audio.mp3'
ARQUIVO_VIDEO_TEMP = PASTA_TEMP / 'video.mp4'

st.set_page_config(
    page_title='Transcript', 
    page_icon='🎙️', 
    layout='wide'
)

    
def transcreve_tab_video():
    prompt_input = st.text_input('(opcional) Insira um prompt para auxiliar a transcrição', key='input_video')
    arquivo_video = st.file_uploader('Adicione um arquivo de vídeo .mp4', type=['mp4'])
    if not arquivo_video is None:
        with open(ARQUIVO_VIDEO_TEMP, mode='wb') as video_f:
            video_f.write(arquivo_video.read())
        moviepy_video = VideoFileClip(str(ARQUIVO_VIDEO_TEMP))
        moviepy_video.audio.write_audiofile(ARQUIVO_AUDIO_TEMP)
        
        with open(ARQUIVO_AUDIO_TEMP, 'rb') as arquivo_audio:
            transcricao = client.audio.transcriptions.create(
                model='whisper-1',
                language='pt',
                response_format='text',
                file=arquivo_audio,
                prompt=prompt_input
            )
            st.write(transcricao)


def transcreve_tab_audio():
    prompt_input = st.text_input('(opcional) Insira um prompt para auxiliar a transcrição', key='input_audio')
    arquivo_audio = st.file_uploader('Adicione um arquivo de áudio .mp3', type=['mp3'])
    
    if not arquivo_audio is None:
        transcricao = client.audio.transcriptions.create(
            model='whisper-1',
            language='pt',
            response_format='text',
            file=arquivo_audio,
            prompt=prompt_input
        )
        st.write(transcricao)


def main():
    st.header('Bem-vindo ao Transcript 🎙️', divider=True)
    st.markdown('#### Transcreva áudios de vídeos e de arquivos de áudio!')
    tab_video, tab_audio = st.tabs(['Vídeo', 'Áudio'])
    
    with tab_video:
        transcreve_tab_video()
    
    with tab_audio:
        transcreve_tab_audio()

if __name__ == '__main__':
    main()