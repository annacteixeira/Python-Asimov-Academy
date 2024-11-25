# Strings são consideradas sequências de caracteres

nome = "Gabriel" 

lista = [1, 2, 3, 4]
print(type(lista))

# Transforma a lista em uma tupla
lista = tuple(lista)
print(type(lista))

print(nome[0])
# >> G

lista_nome = list(nome)
print(lista_nome)
# ['G', 'a', 'b', 'r', 'i', 'e', 'l']

print(type(lista_nome))
# class 'list'

seq = [1, 2, 3]

if seq:
    print("A sequência não está vazia")
else:
    print("A sequência está vazia")