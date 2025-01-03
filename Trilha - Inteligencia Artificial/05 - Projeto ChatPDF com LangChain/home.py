import streamlit as st
from pathlib import Path
import time

FILES_FOLDER = Path(__file__).parent / 'files'

def create_conversation_chain():
    st.session_state['chain'] = True
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
    
def main():
    with st.sidebar:
        sidebar()
    pass

if __name__ == '__main__':
    main()
