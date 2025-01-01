from datasets import load_dataset

ds = load_dataset("stanfordnlp/imdb", streaming=True)

train_ds = ds['train']

print(train_ds[9])

input()

print(train_ds['label'])

input()

print(train_ds[9]['label'])

df = train_ds.to_pandas()
print(df)

for line in train_ds:
    print(line)
    input()
