from transformers import AutoTokenizer
from config import HUGGINGFACE_TOKEN
from huggingface_hub import login

login(token=HUGGINGFACE_TOKEN)

model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

chat = [
    {'role':'user', 'content':'Hello, what is your name?'},
    {'role':'assistant', 'content':'Hi, I am an AI model. How can I help you?'},
    {'role':'user', 'content':'I would like to learn Python. Do you have any tips?'},
]

tokenizer_mixtral = AutoTokenizer.from_pretrained(model)
template_mixtral = tokenizer_mixtral.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

print(template_mixtral)
