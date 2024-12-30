from transformers import pipeline

models = [
    {
        'name':'FacebookAI/xlm-roberta-base',
        'token':'<mask>',
    },
    {
        'name':'neuralmind/bert-base-portuguese-cased',
        'token':'[MASK]',
    },
    {
        'name':'rufimelo/Legal-BERTimbau-base',
        'token':'[MASK]',
    },
]

for dict_model in models:
    name_model = dict_model['name']
    token_model = dict_model['token']
    print(f'Testando modelo {name_model}')
    model = pipeline(task='fill-mask', model=name_model)
    
    quote = f'Este documento é essencial para a {token_model}'
    predictions = model(quote)
    
    for prediction in predictions:
        answer = prediction['token_str']
        score = prediction['score']
        quote = prediction['sequence']
        score_adjusted  = score * 100
        print(f'Prediction "{answer}" with score {score_adjusted:.2f}% -> "{quote}"\n')
    
    input('Press enter to see the next model\n')