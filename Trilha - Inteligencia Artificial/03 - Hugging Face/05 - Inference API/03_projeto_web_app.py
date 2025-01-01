# Miniprojeto - Webapp com múltiplos chatbots

import streamlit as st
import requests
from config import HUGGINGFACE_TOKEN
from transformers import AutoTokenizer

st.set_page_config(
    page_title='Multiple Chatbots', 
    page_icon='🤖', 
)

models = {
    'mistralai/Mixtral-8x7B-Instruct-v0.1':'[/INST]',
    'google/gemma-7b':'<start_of_turn>model\n',
}

model = st.selectbox('Select a model:', options=models)
token_model = models[model]


if (
    'current_model' not in st.session_state # Primeira execução do programa
    or st.session_state['current_model'] != model # Mudança de modelo
    ): 
    st.session_state['current_model'] = model
    st.session_state['messages'] = []
    
model_name = st.session_state['current_model']

tokenizer = AutoTokenizer.from_pretrained(model_name)
url = f'https://api-inference.huggingface.co/models/{model_name}'
messages = st.session_state['messages']

chat_area = st.empty()
user_question = st.chat_input('Ask a question: ')

if user_question:
    messages.append({'role': 'user', 'content': user_question})
    template = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    json = {
        'inputs': template,
        'parameters': {'max_new_tokens': 1000},
        'options': {'use_cache': False, 'wait_for_model': True},
    }

    headers = {
        'Authorization': f'Bearer {HUGGINGFACE_TOKEN}'
    }
    
    response = requests.post(url, json=json, headers=headers).json()
    message_chatbot = response[0]['generated_text'].split(token_model)[-1]
    
    messages.append({'role': 'assistant', 'content': message_chatbot})

with chat_area.container():
    for message in messages:
        chat = st.chat_message(message['role'])
        chat.markdown(message['content'])