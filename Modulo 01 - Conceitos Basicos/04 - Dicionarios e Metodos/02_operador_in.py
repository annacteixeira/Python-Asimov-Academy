capitais = {
    'Brasil':'Brasília', 
    'França':'Paris', 
    'Japão':'Tóquio',
    'Inglaterra':'Londres'
}

print('Brasil' in capitais)
# >> True

pais = 'Inglaterra'

if pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')
else:
    print(f'Não há capital registrada para o país {pais}')
    
print('-' * 100)

# ----------------------------------------------------------------------------------------------------------------------
valores = [1, 2, 3, 4]

print(4 in valores)
# >> True

print('-' * 100)

# ----------------------------------------------------------------------------------------------------------------------

texto = 'Eu estou aprendendo Python na Asimov Academy!'

print('Python' in texto)
# >> True

print('Anna' in texto)
# >> False

print('-' * 100)

# ----------------------------------------------------------------------------------------------------------------------

while True:
    opt = input('Escolha uma opção [1, 2] | q para sair: ')
    
    if opt == 'q':
        break
    elif opt not in ('1', '2'):
        print('Opção inválida. Digite 1 ou 2.')
        continue
    else: 
        print(f'Opção selecionada: {opt}')