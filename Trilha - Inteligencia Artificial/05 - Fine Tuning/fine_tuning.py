import json

with open('respostas.json', encoding="utf8") as f:
    json_respostas = json.load(f)

with open('respostas.jsonl', 'w', encoding="utf8") as f:
    for entrada in json_respostas:
        resposta = {
            'resposta': entrada['resposta'],
            'categoria': entrada['categoria'],
            'fonte': 'AsimoBot'
        }
        entrada_jsonl = {
            'messages': [
                {'role': 'user', 'content': entrada['pergunta']},
                {'role': 'assistant', 'content': json.dumps(resposta, ensure_ascii=False, indent=2)}
            ]
        }
        json.dump(entrada_jsonl, f, ensure_ascii=False)
        f.write('\n')
        
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

file = client.files.create(
    file=open('respostas.jsonl',  'rb'),
    purpose='fine-tune'
)

client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)

client.fine_tuning.jobs.list()


# Utilizando o modelo

system_mes = '''
Responda as perguntas em um parágrafo de até 20 palavras. Categorize as respostas no seguintes conteúdos: física, matemática, língua portuguesa ou outros.
Retorne a resposta em um formato json, com as keys: 
fonte: valor deve ser sempre AsimoBot
resposta: a resposta para a pergunta
categoria: a categoria da pergunta
'''

mensagens = [
    {'role':'system', 'content': system_mes},
    {'role':'user', 'content':'O que é uma equação quadrática?'}
]

resposta = client.chat.completions.create(
    messages=mensagens,
    model='ft:gpt-3.5-turbo-0125:personal::AgBHu5rm',
    max_tokens=1000,
    temperature=0
)

print(resposta.choices[0].message.content)
print (resposta.usage)