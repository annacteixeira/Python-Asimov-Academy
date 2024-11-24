# Dada uma sequência de números, calcule a soma e a média dos números.
# ATENÇÃO: não vale usar a função sum()

print('-' * 100)

sequencia_numerica = int(input('\nInforme quantos números você deseja digitar: \n'))
soma = 0
media = 0
contador = 0

for i in range(1, sequencia_numerica + 1):
    numero = int(input(f'\nInforme o {i}º valor: '))
    soma += numero
    contador += 1
    
media = soma / contador

print(f'\nSoma dos números = {soma}\nMédia dos números = {media}\n')
    
print('-' * 100)

# Dada uma sequência de números, calcule o maior valor da sequência
# ATENÇÃO: não vale usar a função max()

sequencia_numerica_01 = int(input('\nInforme quantos números você deseja digitar: \n'))

maior = 0

for i in range(1, sequencia_numerica_01 + 1):
    numero_01 = int(input(f'\nInforme o {i}º valor: '))
    
    if i == 1:
        maior = numero_01

    if numero_01 > maior:
        maior = numero_01
        
print(f'\nMaior número = {maior}\n')

print('-' * 100)


# Dada uma lista de palavras, printe todas as palavras com pelo menos 5 caracteres

palavras = ['abacate', 'banana', 'cereja', 'tomate', 'uva', 'melao', 'kiwi']

for palavra in palavras:
    if len(palavra) >= 5:
        print(palavra)