from transformers import pipeline

model = 'facebook/mbart-large-50-many-to-many-mmt'

messages = [
    'Olá! Estou aprendendo a programar em Python e a usar modelos de Inteligência Artificial.',
    'Vamos nos encontrar às 15h da próxima sexta-feira. Eu acho que todos os meus amigos vão estar lá!',
    'Três tigres tristes comeram pratos de trigo',
    'Ser feliz sem motivo é a mais autêntica forma de felicidade',
]

languages = [
    'en_XX',
    'es_XX',
    'fr_XX'
]

translator = pipeline(task='translation', model=model)

for language in languages:
    print(f'\n\nTraduzindo para {language}...')
    translations = translator(messages, src_lang='pt_XX', tgt_lang=language) 
    for message, translation in zip(messages, translations):
        print('Frase original:', message)
        sentence_translated = translation['translation_text']
        print(f'Frase em língua {language}: "{sentence_translated}"')
