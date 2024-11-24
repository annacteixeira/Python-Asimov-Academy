pessoas = ['João', 'Paulo', 'Clara', 'Maria']

# O slicing parte do primeiro elemento selecionado e vai até o último, sem incluí-lo
print(pessoas[1:3])
# ['Paulo', 'Clara']

# Faz slicing até o último elemento da lista
print(pessoas[1:])

# Faz o slicing do primeiro até o elemento de índice desejado, sem incluí-lo
print(pessoas[:3])

nome = 'Juliano'
print(nome[1:])
# >> 'liano'

print(nome[:-1])
# >> 'Julian'

print(nome[2:5])
# >> 'lia'

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Faz o slicing pulando de 2 em 2
print(numeros[0:len(numeros):2])
# OU:
print(numeros[::2])

# Imprime a lista de traz para frente
print(numeros[::-1])
# >> [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(numeros[::-2])
# >> [9, 7, 5, 3, 1]