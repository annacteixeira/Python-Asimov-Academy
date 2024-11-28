# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X jogadores, de forma que cada
# jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de cada jogador e mostra quais são.

# DICA: utilize os símbolos ♠ ♣ ♥ ♦ para representar os naipes
# DICA: utilize a função random.shuffle (módulo random) para embaralhar

import random

def gerar_baralho():
    
    baralho = [
        '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
        '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
        '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
        '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K'
]

    coringas = ['C1', 'C2']
    adicionar_coringas = input('\nVocê quer adicionar coringas ao baralho? [S/N]: ').lower()

    if adicionar_coringas == 's':
        baralho.extend(coringas)

    quantidade_baralhos = int(input('Quantos baralhos você deseja gerar? '))

    baralho_final = []

    for i in range(quantidade_baralhos):
        baralho_final.extend(baralho.copy())

    embaralhar = input('\nVocê quer embaralhar os baralhos? [S/N]: ').lower()

    if embaralhar == 's':
        random.shuffle(baralho_final)

    return baralho_final

def mostrar_baralho(cartas):
    print('\n============ BARALHOS ==========')
    print(f'O baralho tem {len(cartas)} cartas')
    
    print(cartas)

def dar_as_cartas(cartas):
    jogadores = int(input('\nQuantas pessoas irão jogar? '))
    
    lista_jogadores = [[]for _ in range(jogadores)]
    
    quantidade_cartas = int(input('Quantas cartas cada pessoa deve receber? '))
    
    total_cartas_distribuidas = quantidade_cartas * jogadores
    
    while total_cartas_distribuidas > len(cartas):
        print(f'Erro! O baralho só possui {len(cartas)} cartas restantes.')
        quantidade_cartas = int(input('Quantas cartas cada pessoa deve receber? '))
        total_cartas_distribuidas = quantidade_cartas * jogadores
        
    for j in range(jogadores):
        for _ in range(quantidade_cartas):
            carta = cartas.pop(random.randint(0, len(cartas) - 1))
            lista_jogadores[j].append(carta)
            
    return lista_jogadores

def mostrar_jogadores(lista_jogadores):
    print('\n========== MÃO DE CADA JOGADOR ==========')
    for i, jog in enumerate(lista_jogadores):
        print(f'Jogador {i + 1} possui {len(jog)} cartas: {', '.join(jog)}')


def main():
    cartas = gerar_baralho()
    mostrar_baralho(cartas)
    
    jogadores = dar_as_cartas(cartas)
    
    mostrar_baralho(cartas)
    
    mostrar_jogadores(jogadores)


main()