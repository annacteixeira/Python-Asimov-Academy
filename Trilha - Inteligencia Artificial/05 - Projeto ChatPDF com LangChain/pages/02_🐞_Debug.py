import streamlit as st
from langchain.prompts import PromptTemplate
from configs import get_config

st.set_page_config(
    page_title='Debug',
    page_icon='🐞',
)


def debug_page():
    st.header('🐞 Página de Debug', divider=True)
    prompt_template = get_config('prompt')
    prompt_template = PromptTemplate.from_template(prompt_template)
    
    if not 'last_answer' in st.session_state:
        st.error('Faça uma pergunta para o modelo para visualizar o debug')
        st.stop()
        
    last_answer = st.session_state['last_answer']
    
    context_docs = last_answer['source_documents']
    context_list = [doc.page_content for doc in context_docs]
    context_str = '\n\n'.join(context_list)
    
    chain = st.session_state['chain']
    memory = chain.memory
    
    chat_history = memory.buffer_as_str
    
    with st.container(border=True):
        prompt = prompt_template.format(
            chat_history=chat_history,
            context=context_str,
            question=''
        )
        st.code(prompt)
    
    
debug_page()