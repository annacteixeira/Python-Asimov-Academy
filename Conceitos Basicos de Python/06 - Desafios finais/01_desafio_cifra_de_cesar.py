# Crie um código que implementa a 'Cifra de César', isto é,
# que transforma uma string movendo cada letra um certo número de passos no alfabeto.
# O número de passos é dado por uma chave.
# Letras com acentos, espaços e pontuação permanecem iguais.

# Exemplos: 
# 'abc' com chave 1 = 'bcd'
# 'ABCDE' com chave 2 = 'CDEFG'
# 'Cachorro' com chave 1 = 'Bzbgnqqn'

# DICA: Construa duas strings com as letras do alfabeto em ordem,
# uma para letras minúsculas e outra para letras maiúsculas, e use esta string
# para guiar as substituições

def cifrar_caractere(caractere, sequencia, chave):
    indice_atual = sequencia.index(caractere)
    novo_indice = indice_atual + chave
    
    while novo_indice >= len(sequencia):
        novo_indice = novo_indice - len(sequencia)
        
    while novo_indice < 0:
        novo_indice = novo_indice + len(sequencia)
        
    return sequencia[novo_indice]

alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('\n')
frase_original = input('Digite um texto qualquer para descobrir a sua Cifra de César: ')
chave = int(input('Informe o valor da chave para deslocar o texto: '))
# operacao = input('Escolha [C] para criptografar o texto e [D] para descriptografar')
cifra = ''
    

for caractere in frase_original:
    if caractere in alfabeto_minusculo:
        caractere_cifra = cifrar_caractere(caractere, alfabeto_minusculo, chave)
    elif caractere in alfabeto_maiusculo:
        caractere_cifra = cifrar_caractere(caractere, alfabeto_maiusculo, chave)
    else:
        caractere_cifra = caractere

    cifra = cifra + caractere_cifra
    
print(f'Texto cifrado: {cifra}')
    
