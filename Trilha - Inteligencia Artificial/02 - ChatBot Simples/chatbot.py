import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-3.5-turbo-0125',
    temperature=0,
    max_tokens=1000,
    stream=True
)

    texto_completo = ''

    print('Assistant: ', end='')
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
            
    mensagens.append({'role':'assistant', 'content':texto_completo})
    return mensagens

    
if __name__ == '__main__':
    
    print('\nBem-vindo ao chatbot com Python :)\n')
    mensagens = []
    while True:
        input_usuario = input('User: ')
        mensagens.append({'role':'user', 'content':input_usuario})
        mensagens = geracao_texto(mensagens)
        print('\n')