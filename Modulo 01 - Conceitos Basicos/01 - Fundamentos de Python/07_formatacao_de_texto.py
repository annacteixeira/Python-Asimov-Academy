nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
idade_daqui_5_anos = idade + 5

# Print formatted -> igual C, porém o 'f' vem dentro dos parênteses
print(f'Olá, {nome}!')

# Casas decimais: :.2f -> igual C só que com os ':'
print(f'Seu nome possui {len(nome):.2f} letras')
print(f'Daqui 5 anos voce tera {idade_daqui_5_anos} anos')

# Quebra de linha: igual C
print('Este é um exemplo de\nQuebra de linha')

# print(r'Texto') -> O r vem de raw. O python ignora os caracteres de escape
print(r'Aqui, o \n não irá funcionar e aparecerá como texto bruto')

# Imprimindo uma string várias vezes
print('---' * 15)
