valores = [10, 20, 30, 3, -2, 17]

for valor in valores:
    print(f'O valor é: {valor}')
    
print('Acabou o loop\n')

# ----------------------------------------------------------------------------------
nome = 'Juliano'

for caractere in nome:
    print(f'O caractere é: {caractere}')

print('Acabou o nome\n')

# ----------------------------------------------------------------------------------

clientes = [
    ('Ana', '123.456.789-00', 'ana@email.com'), 
    ('Luiz', '111.222.333-00', 'luiz@email.com')
]

for nome, cpf, email in clientes:
    print(f'Cliente: {nome}\tCPF: {cpf}\tE-mail: {email}')
    
    # OU: 
    # nome = cliente[0]
    # cpf = cliente[1]
    # email = cliente[2]
    
    # OU:
    # nome, cpf, email = cliente

