from transformers import pipeline

model = 'facebook/mbart-large-50-many-to-many-mmt'

message = 'Olá! Estou aprendendo a programar em Python e a usar modelos de IA.'

translator = pipeline(task='translation', model=model)

translation = translator(message)