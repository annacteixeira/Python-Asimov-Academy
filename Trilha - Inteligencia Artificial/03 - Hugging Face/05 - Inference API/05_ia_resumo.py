import requests
from config import HUGGINGFACE_TOKEN

model = 'csebuetnlp/mT5_multilingual_XLSum'
url = f'https://api-inference.huggingface.co/models/{model}'

with open('assets/brasil.txt', encoding='utf8') as f:
    text = f.read()

json = {
    'inputs': text,
    'parameters': {'min_length': 200},
    'options': {'use_cache': False, 'wait_for_model': True},
}

headers = {
    'Authorization': f'Bearer {HUGGINGFACE_TOKEN}'
}

response = requests.post(url, json=json, headers=headers)

print(response.json())
