n = 0

while n < 10:
    print(f'O valor de n é: {n}')
    n += 1
    
    if n == 5:
        break
    
print('\nO loop acabou!\n')

# ------------------------------------------------------------------------------

for n in range(-5, 6):
    print(f'\n{n}')
    if n == 0:
        continue
    
    resultado = 1 / n
    print(f'O resultado é: {resultado}')
    
print('\nO loop acabou!')

# ------------------------------------------------------------------------------

while True:
    entrada = input('Digite qualquer coisa [q - para sair]: ')
    print(f'O valor digitado foi: {entrada}\n')
    
    if entrada == 'q':
        break
    
print('\nPrograma finalizado\n')

# ------------------------------------------------------------------------------

while True:
    opt = input('Escolha uma opção [1, 2] | [q - para sair]: ')
    if opt == 'q':
        break
    elif opt != '1' and opt != '2':
        print(f'A opção {opt} é inválida')
        continue
    print(f'Opção selecionada: {opt}')
        