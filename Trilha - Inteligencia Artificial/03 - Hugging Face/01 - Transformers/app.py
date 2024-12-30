from transformers import pipeline

model = pipeline('fill-mask')

quote = 'The capital of <mask> is Brasília.'

predictions = model(quote)
for prediction in predictions:
    answer = prediction['token_str']
    score = prediction['score']
    quote = prediction['sequence']
    score_adjusted  = score * 100
    print(f'Prediction "{answer}" with score {score_adjusted:.2f}% -> "{quote}"')