from dotenv import load_dotenv
import streamlit as st
import time

from utils import initialize_api_openai, create_conversation_chain, FILES_FOLDER

load_dotenv()

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
        
    chain = st.session_state['chain']
    memory = chain.memory
    
    messages = memory.load_memory_variables({})['chat_history']
    
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
        
        chain.invoke({'question': new_message})
        time.sleep(2)
        
        st.rerun()
        
    
def main():
    with st.sidebar:
        sidebar()
    chat_window()
    initialize_api_openai()

if __name__ == '__main__':
    main()
