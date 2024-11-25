# Listas são sequências de elementos
# [1, 2, 3, 4]

lista1 = [1, 2, 3, 4]
lista2 = [1, 1.0, True, "Python"]
lista_misturada = [0, 1.1, "Python", True, [1, 2]]
alunos = ['Anna', 'Bruno', 'Carlos']
vendas = [50, 40, 45, 30]


print(type(lista1))
# >> class 'list'

print(alunos[0])
# >> Anna

# Buscando o último elemento da lista
print(alunos[len(alunos) - 1])
# >> Carlos

print(alunos[-1])
# >> Carlos

print(lista_misturada[-1])
# >> [1, 2]

# Remove o item da lista de índice 0
del alunos[0]
print(alunos)
# >> ['Bruno', 'Carlos'']

