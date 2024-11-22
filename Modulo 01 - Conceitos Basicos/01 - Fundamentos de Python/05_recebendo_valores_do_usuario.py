# Podemos receber valores do usuário utilizando a função input()
# A função input() trata as entradas como STRINGS

print("Informe a sua nota")
nota = int(input())

print(nota)
print(type(nota))

# Podemos passar como argumento o prompt, dizendo ao usuário o que ele deve digitar

nome = input("Digite seu nome: ")
print(nome)
print(type(nome))