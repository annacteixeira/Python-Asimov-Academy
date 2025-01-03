from pathlib import Path
from langchain.memory import ConversationBufferMemory

import streamlit as st
import time

FILES_FOLDER = Path(__file__).parent / 'files'

def create_conversation_chain():
    st.session_state['chain'] = True
    
    memory = ConversationBufferMemory(return_messages=True)
    memory.chat_memory.add_user_message('Oi')
    memory.chat_memory.add_ai_message('Oi, eu sou uma LLM!')
    st.session_state['memory'] = memory
    
    time.sleep(1)

def sidebar():
    uploaded_pdfs= st.file_uploader(
        'Adicione seus arquivos PDF', 
        type=['.pdf'], 
        accept_multiple_files=True
    )
    
    if not uploaded_pdfs is None:
        for arquivo in FILES_FOLDER.glob('*.pdf'):
            arquivo.unlink()
        
        for pdf in uploaded_pdfs:
            with open(FILES_FOLDER / pdf.name, 'wb') as f:
                f.write(pdf.read())
    
    button_label = 'Inicializar ChatBot'
    if 'chain' in st.session_state:
        button_label = 'Atualizar ChatBot'
    
    if st.button(button_label, use_container_width=True):
        if len(list(FILES_FOLDER.glob('*.pdf'))) == 0:
            st.error('Adicione pelo menos um arquivo PDF para inicializar o ChatBot')
        else:
            st.success('Inicializando o ChatBot...')
            create_conversation_chain()
            st.rerun()
    
def chat_window():
    st.header('🤖 Chat com PDFs', divider=True)
    
    if not 'chain' in st.session_state:
        st.error('Faça o upload de PDFs para começar!')
        st.stop()
        
    # chain = st.session_state['chain']
    # memory = chain.memory
    
    memory = st.session_state['memory']
    messages = memory.load_memory_variables({})['history']
    
    container = st.container()
    for message in messages:
        chat = container.chat_message(message.type)
        chat.markdown(message.content)
    
    new_message = st.chat_input('Converse com seus documentos...')
    
    if new_message:
        chat = container.chat_message('human')
        chat.markdown(new_message)
        
        chat = container.chat_message('ai')
        chat.markdown('Gerando resposta...')
        
        time.sleep(2)
        
        memory.chat_memory.add_user_message(new_message)
        memory.chat_memory.add_ai_message('Oi, eu sou uma LLM!')
        st.rerun()
        
    
def main():
    with st.sidebar:
        sidebar()
    chat_window()

if __name__ == '__main__':
    main()
