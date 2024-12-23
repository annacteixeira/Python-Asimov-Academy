import openai

# SALVAMENTO E LEITURA DE CONVERSAS =====================================
def retorna_resposta_modelo(mensagens, 
                            openai_key, 
                            modelo='gpt-3.5-turbo',
                            temperatura=0,
                            stream=False):
    openai.api_key = openai_key
    response = openai.chat.completions.create(
        model = modelo,
        messages = mensagens,
        temperature = temperatura,
        stream = stream
    )
    
    return response
