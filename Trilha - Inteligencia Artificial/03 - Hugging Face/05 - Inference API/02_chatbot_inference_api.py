import requests

from transformers import AutoTokenizer
from config import HUGGINGFACE_TOKEN
from huggingface_hub import login

login(token=HUGGINGFACE_TOKEN)

model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

chat = []

tokenizer = AutoTokenizer.from_pretrained(model)


url = f'https://api-inference.huggingface.co/models/{model}'

while True:
    message = input('User: (or "q" to finish the conversation): ')
    
    if message == 'q' or message == 'Q':
        break
    
    chat.append({'role': 'user', 'content': message})
    template = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    
    json = {
        'inputs': template,
        'parameters': {'max_new_tokens': 1000},
        'options': {'use_cache': False, 'wait_for_model': True},
    }

    headers = {
        'Authorization': f'Bearer {HUGGINGFACE_TOKEN}'
    }
    
    response = requests.post(url, json=json, headers=headers).json()
    message_chatbot = response[0]['generated_text'].split('[/INST]')[-1]
    print('Assistant:', message_chatbot)
    
    chat.append({'role': 'assistant', 'content': message_chatbot})
