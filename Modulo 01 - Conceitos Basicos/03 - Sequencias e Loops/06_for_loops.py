for n in range(10):
    print(f'O valor de n é: {n}')
    
for _ in range(5):
    print('Olá!')
    
# Refazendo o desafio com o loop for - crie um programa que
    # - Escolhe um número secreto
    # - Pede por um chute do usuário
    # - Indica se o usuário acertou ou não
    # - Se não acertou, dá uma dica, dizendo se o número é mais alto ou mais baixo
    # - Repete isso até 3 vezes
    
numero_secreto = 33
descobriu = False

for _ in range(3):
    if not descobriu:
        numero_chute = int(input('\nDescubra o número!\nSeu chute: '))
        if numero_chute < numero_secreto:
            print('\nSeu chute é menor que o número secreto')
    
        elif numero_chute > numero_secreto:
            print('\nSeu chute é maior que o número secreto')
    
        else:
            print('\nVocê descobriu!')
            descobriu = True


if descobriu:
    print('\nParabéns, você ganhou!\n')
else:
    print(f'\nQue pena,você perdeu. Acabaram as suas chances.\nO número secreto era {numero_secreto}\n')