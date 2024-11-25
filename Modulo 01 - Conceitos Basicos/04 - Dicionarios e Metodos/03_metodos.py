# Métodos de Strings:

print('\nStrings')

frase_01 = 'Olá MunDo!'

print(frase_01.upper())
# >> OLÁ MUNDO!

print(frase_01.lower())
# >> olá mundo!

arquivo = '2023_01_01_NotaFiscal.pdf'
print(arquivo.endswith('.pdf'))
# >> True

print(arquivo.endswith('.docx'))
# >> False

print(arquivo.startswith('2023'))
# >> True

print(arquivo.startswith('2022'))
# >> False


if arquivo.startswith('2023') and arquivo.endswith('.pdf'):
    print('Nota fiscal encontrada!')

# >> Nota fiscal encontrada!

texto = 'Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia!'
print(texto.count('a'))
# >> 7

print(texto.count('dia'))
# >> 4 -> Observação: Não contou 'Dia', por causa da letra maiúscula

print(texto.lower().count('dia'))
# >> 5

print('\n')

# O método find() retorna o índice da posição onde foi encontrado o caractere desejado.
# Só retorna a primeira ocorrência
seq = 'aaaaaaaaaaaaaaabbbbbbbbbbaaaaaaaaaaaabbbbbbbbbbb'
print(seq.find('b'))
# >> 15 

# Caso o caractere não exista na string, o método find() retorna -1
print(seq.find('c'))
# >> -1

print(seq.index('b'))
# >> 15

# Caso o caractere não exista na string, o método index() retorna um erro
# print(seq.index('c'))
# >> ValueError: substring not found

print(seq[seq.find('b'):])
# >> bbbbbbbbbbaaaaaaaaaaaabbbbbbbbbbb

# O método isdigit() retorna True caso a string seja composta apenas por números
string_numerica = '1234567890'
print(string_numerica.isdigit())
# >> True

# O método isalpha() retorna True caso a string seja composta apenas por letras do alfabeto
string_letras = 'abcdEFGhij'
print(string_letras.isalpha())

string_misturada = 'Olá 2023 Python!'
print(string_misturada.isdigit())
# >> False

print(string_misturada.isalpha())
# >> False

frase_02 = 'Estou estudando Python!'
frase_02 = frase_02.replace('!', '?') 
print(frase_02)
# >> Estou estudando Python?

frase_02 = frase_02.replace('u', 'xxxxx')
print(frase_02)
# >> Estoxxxxx estxxxxxdando Python?

frase_02 = frase_02.replace('Python', 'C#')
print(frase_02)
# >> Estoxxxxx estxxxxxdando C#?

frase_03 = 'Estou estudando Python \n\n\n Este curso é muito bom!'
frase_03 = frase_03.replace('\n', '').replace(' ', '')
print(frase_03)
# >> EstouestudandoPythonEstecursoémuitobom!

# O método split() divide uma string em uma lista onde cada palavra é um item da lista
# Por padrão, o split() separa com base nos espaços em branco
linha_01 = 'Item1   Item2   Item3'
print(linha_01.split())
# >> ['Item1', 'Item2', 'Item3']

# Podemos especificar o separador
linha_02 = 'Item1;Item2;Item3'
print(linha_02.split(';'))
# >> ['Item1', 'Item2', 'Item3']

# O método join em Python é usado para concatenar os elementos de um iterável (como uma lista ou tupla) em uma única string, utilizando um separador definido.
# Ele é chamado sobre a string que será utilizada como separador.

nomes = ['Joana', 'Marcelo', 'Paulo']
print('-------'.join(nomes))
# >> Joana-------Marcelo-------Paulo

print('\n')
# =================================================================================================================

# MÉTODOS DE NÚMEROS:
print('\nNúmeros')

decimal = 4.5

# O método as_integer_ratio()  converte um número decimal em uma fração representada por dois números inteiros
# A fração gerada é irredutível, ou seja, já está simplificada
# O método retorna uma tupla no formato (numerador, denominador)

print(decimal.as_integer_ratio())
# >> (9, 2)

# Retorna True se a instância float for finita com valor integral, e False caso contrário.
print(decimal.is_integer())
# >> False

y = 4.9
int(y)

print(y.is_integer())
# >> False

z = 10
print(z.is_integer())
# >> True

print('\n')

# =================================================================================================================

# MÉTODOS DE LISTAS:
print('\nListas')

lista_01 = [1, 2, 3]
lista_02 = lista_01.copy()

print(lista_01)
# >> [1, 2, 3]
print(lista_02)
# >> [1, 2, 3]

lista_02.clear()
print(lista_02)
# >> []

for i in range(5):
    lista_02.append(i * 2)

print(lista_02)
# >> [0, 2, 4, 6, 8]

lista_02.append('hello')
print(lista_02)
# >> [0, 2, 4, 6, 8, 'hello']

valores = [10, 30, -90, -1, 0, 1]

valores_positivos = []

for valor in valores:
    if valor >= 0:
        valores_positivos.append(valor)
        
print(valores_positivos)
# >> [10, 30, 0, 1]

numeros = [1, 2, 3]
numeros.append([4, 5, 6])
print(numeros)
# >> [1, 2, 3, [4, 5, 6]]

numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros)
# >> [1, 2, 3, 4, 5, 6]

novos_numeros = numeros + [7, 8 ,9]
print(novos_numeros)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]

vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
print(vogais)
# >> ['a', 'e', 'i', 'o', 'u']

# O método pop() remove o último valor de uma lista
novos_valores = [150, 20, 30, 40, 50]
valor_removido = novos_valores.pop()
print(valor_removido)
# >> 50

print(novos_valores)
# >> [150, 20, 30, 40]

# Podemos passar o índice no método pop() para remover um valor específico
valor_removido = novos_valores.pop(0)
print(valor_removido)
# >> 150

print(novos_valores)
# >> [20, 30, 40]

clientes = ['www', 'xxx', 'yyy']
while clientes:
    cliente = clientes.pop()
    print(f'Processando cliente {cliente}')

# Processando cliente yyy
# Processando cliente xxx
# Processando cliente www

digitos = [150, 30, 50, 75, 45, 90]

digitos.reverse()
print(digitos)
# >> [90, 45, 75, 50, 30, 150]

# O método sort() ordena os valores.
digitos.sort()
print(digitos)
# >> [30, 45, 50, 75, 90, 150]

print('\n')
# =================================================================================================================

# MÉTODOS DE TUPLAS:
print('\nTuplas')

tupla = ('A', 'B', 'C')

print(tupla.index('A'))
# >> 0

print(tupla.count('C'))
# >> 1

print('\n')
# =================================================================================================================

# MÉTODOS DE DICIONÁRIOS:
print('\nDicionários')

dicionario = {'chave1':'valor1', 'chave2':'valor2', 'chave3':'valor3'}

produtos = {
    'banana':3.60, 
    'leite':4.90, 
    'carne':15.50, 
    'pão':9.00
}

# Buscando pelo valor de uma chave
print(produtos.get('banana'))
# >> 3.6

resultado_01 = produtos.get('leite')
print(resultado_01)
# >> 4.9

resultado_02 = produtos.get('arroz')
print(resultado_02)
# >> None

# Caso a chave não exista, podemos usar a função get para retornar uma mensagem
print(produtos.get('arroz', 'Essa chave não existe no dicionário'))
# >> Essa chave não existe no dicionário

# O método setdefault() retorna o valor do item com a chave especificada
# Sintaxe: dictionary.setdefault(keyname, value)
metodo_set_default_01 = produtos.setdefault('banana', 100)
print(metodo_set_default_01)
# >> 3.6

# Caso a chave não exista, o setdefault pode ser usado para adicioná-la ao dicionário, usando setdefault(chave, valor)
metodo_set_default_02 = produtos.setdefault('arroz', 100)
print(metodo_set_default_02)
# >> 100

print(produtos)
# >> {'banana': 3.6, 'leite': 4.9, 'carne': 15.5, 'pão': 9.0, 'arroz': 100}

print('\n')
# O método keys permite iterar sobre as chaves do dicionário de maneira mais simples
for produto in produtos.keys():
    print(produto)

print('\n')

# O método values permite iterar sobre os valores do dicionário de maneira mais simples

for valor in produtos.values():
    print(valor)
    
print('\n')

# O método items permite iterar sobre o dicionário, retornando seus pares chave-valor.
# Ele retorna tuplas de dois elementos (chaves e seus respectivos valores)
for k, v in produtos.items():
    print(f'{k} -> {v}')
    
print('\n')


novos_produtos = {
    'massa': 5.70,
    'banana': 4.40
}

# O método update() é utilizado para adicionar elementos de um dicionário em outro dicionário. 
# Ele recebe como parâmetro outro dicionário e adiciona seus elementos ao dicionário atual.
produtos.update(novos_produtos)
print(produtos)
# >> {'banana': 4.4, 'leite': 4.9, 'carne': 15.5, 'pão': 9.0, 'arroz': 100, 'massa': 5.7}

# O método copy() em Python é utilizado para criar uma cópia independente de um dicionário existente
produtos_copia = produtos.copy()
produtos_copia['morango'] = 3.30

print(produtos)
# >> {'banana': 4.4, 'leite': 4.9, 'carne': 15.5, 'pão': 9.0, 'arroz': 100, 'massa': 5.7}

print(produtos_copia)
# >> {'banana': 4.4, 'leite': 4.9, 'carne': 15.5, 'pão': 9.0, 'arroz': 100, 'massa': 5.7, 'morango': 3.3}

# Esvaziando um dicionário
produtos.clear()

print(produtos)
# >> {}
