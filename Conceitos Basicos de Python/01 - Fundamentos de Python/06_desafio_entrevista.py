# Desafio - crie um programa que:
    # 01. Pede pelo seu nome e idade
    # 02. Dá oi para você
    # 03. Conta quantas letras seu nome possui
    # 04. Fala quantos anos você terá daqui a 5 anos
    
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
idade_daqui_5_anos = idade + 5


print("Oi, " + nome)

# convertendo ints para strings para ser possível concatenar
print("Seu nome possui " + str(len(nome)) + " letras")
print("Daqui 5 anos voce tera " + str(idade_daqui_5_anos) + " anos")
