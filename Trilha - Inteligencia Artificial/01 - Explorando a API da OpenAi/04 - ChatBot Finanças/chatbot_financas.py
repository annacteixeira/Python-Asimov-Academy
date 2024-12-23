import json
import yfinance as yf

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

# Definindo as funções

def retorna_coracao_historica(ticker, periodo = '1mo'):
    
    ticker = ticker.replace('.SA', '')
    ticker_obj = yf.Ticker(f'{ticker}.SA')
    hist = ticker_obj.history(period = periodo, auto_adjust = False)['Close']
    hist.index = hist.index.strftime('%Y-%m-%d')
    hist = round(hist, 2)
    
    if len(hist) > 30:
        slice_size = int(len(hist) / 30)
        hist = hist.iloc[::-slice_size][::-1]
    return hist.to_json()

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'retorna_cotacao_historica',
            'description': 'Retorna a cotação diária histórica para uma ação da BOVESPA',
            'parameters':{
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'O ticker da ação. Exemplo: ABEV3 para Ambev, PETR4 para Petrobras, etc',
                    },
                    'periodo': {
                        'type': 'string',
                        'description': 'O período que será retornado dados históricos \
                                        sendo 1mo equivalente a um mês de dados, 1d a um dia \
                                        e 1yo a um ano',
                        'enum':["1d", "5d", "1mo", "6mo", "1y", "5y", "10y", "ytd", "max"]
                    }
                }
            }
        }
    }
]

funcoes_disponiveis = {'retorna_cotacao_historica': retorna_coracao_historica}

def gera_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo-0125',
        tools=tools,
        tool_choice='auto'
    )

    tool_calls = resposta.choices[0].message.tool_calls

    if tool_calls:
        mensagens.append(resposta.choices[0].message)
        for tool_call in tool_calls:
            func_name = tool_call.function.name
            function_to_call = funcoes_disponiveis[func_name]
            func_args = json.loads(tool_call.function.arguments)
            func_return = function_to_call(**func_args)
            
            mensagens.append({
                'tool_call_id': tool_call.id,
                'role': 'tool',
                'name': func_name,
                'content': func_return
            })
        segunda_resposta = client.chat.completions.create(
            messages=mensagens,
            model='gpt-3.5-turbo-0125'
        )
        
        mensagens.append(segunda_resposta.choices[0].message)
    print(f'Assistant: {mensagens[-1].content}')

    return mensagens

if __name__ == '__main__':
    
    print('\nBem-vindo ao ChatBot Financeiro da Asimov\n')
    
    while True:
        input_usuario = input('User: ')
        mensagens = [{'role':'user', 'content':input_usuario}]
        mensagens = gera_texto(mensagens)
        print('\n')