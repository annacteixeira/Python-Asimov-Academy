# Dicionários associam chaves à valores -> par chave-valor (key-value)
# Dicionários são MUTÁVEIS
# Os dicionários não podem ter chaves REPETIDAS

capitais = {
    'Brasil':'Brasília', 
    'França':'Paris', 
    'Japão':'Tóquio'
}

print(capitais)
# >> {'Brasil': 'Brasília', 'França': 'Paris', 'Japão': 'Tóquio'}

print(capitais['Brasil'])
# >> Brasília

print(capitais['França'])
# >> Paris

print(capitais['Japão'])
# >> Tóquio

# print(capitais['Estados Unidos'])
# >> KeyError: 'Estados Unidos' -> Não funciona porque a chave 'Estados Unidos' não está no dicionário

capitais['Inglaterra'] = 'Londres'

print(capitais['Inglaterra'])
# >> Londres

print(capitais)
# >> {'Brasil': 'Brasília', 'França': 'Paris', 'Japão': 'Tóquio', 'Inglaterra': 'Londres'}

# Deletando uma chave: 
del capitais['Inglaterra']

print(capitais)
# >> {'Brasil': 'Brasília', 'França': 'Paris', 'Japão': 'Tóquio'}

# ==========================================================================================================================

# Ao iterar sobre um dicionário, passamos sobre suas chaves
# A iteração ocorre na mesma ordem em que as chaves foram inseridas no dicionário

print('\n')
for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')

print('\n')

# ==========================================================================================================================

# Criando um dicionário vazio
dicionario = {}

# OU: dicionario = dict()

dicionario[10] = 'abc'
dicionario['CHAVE'] = 'VALOR'
dicionario[3.15] = True

print(dicionario)

print('\n')
for chave in dicionario:
    valor = dicionario[chave]
    print(f'Chave: {chave}\tValor: {valor}')
    
print('\n')