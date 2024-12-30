from transformers import AutoTokenizer, AutoModel, pipeline

model_name = 'FacebookAI/xlm-roberta-base'

model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

inputs = tokenizer('A linguagem <mask> é uma ferramenta inovadora', return_tensors='pt')
print(inputs)

outputs = model(**inputs)
print(outputs)