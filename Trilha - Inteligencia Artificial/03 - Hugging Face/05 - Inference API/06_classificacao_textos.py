from transformers import pipeline

model = 'lxyuan/distilbert-base-multilingual-cased-sentiments-student'

reviews = [
    "Até então não tenho do que reclamar. Estou usando pra estudo, está bem tranquilo até aqui.",
    "Acho que vale o custo benefício, caso seja para usos básicos.",
    "A bateria do notebook está descarregando muito rápido.",
    "Eu estava com muito medo de me arrepender da compra. Mas eu realmente gostei! Ótimo demais, comprem!",
    "Muito bom, recomendo!",
    "Não comprem, caro demais pelo que oferece.",
    "Super custo benefício, pelo preço que paguei superou todas as minhas expectativas.",
    "Excelente, zero arrependimentos. Muito muito bom.",
    "Esperava um pouco mais. Mas é um produto bom. Não coloquei mais estrelas pois não usei direito.",
]

classifier = pipeline('text-classification', model=model, top_k=None)

for review in reviews:
    print('Review:', review)
    result = classifier(review)
    
    probability = result[0][0]['score'] * 100
    
    print('Sentimental analysis:', result[0][0]['label'], probability, '\n')