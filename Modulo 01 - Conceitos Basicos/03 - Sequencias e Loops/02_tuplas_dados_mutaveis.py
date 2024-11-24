# Tuplas são imutáveis, ou seja, não conseguimos mudar seus valores

valores = (1, 2, 3)

print(type(valores))
# >> class 'tuple'

# valores[0] = 3
# >> TypeError: 'tuple' object does not support item assignment

