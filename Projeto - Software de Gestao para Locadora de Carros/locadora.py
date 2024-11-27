import os

portfolio = {
    'Chevrolet Tracker':120,
    'Chevrolet Onix':90,
    'Chevrolet Spin':150,
    'Hyundai HB20':85,
    'Hyunday Tucson':120,
    'Fiat Uno':60,
    'Fiat Mobi':70,
    'Fiat Pulse':130
}

carros_alugados = {}


def menu_inicial():
    print('=' * 15)
    print('Bem vindo à locadora de carros!')
    print('=' * 15)
    
    while True:
        opcao_menu = int(input('O que deseja fazer?\n0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro\n'))
        if opcao_menu in [0, 1, 2]:
            return int(opcao_menu)
        print('\nOpcao invalida! Tente novamente.\n')    
    return opcao_menu


def mostrar_portfolio():
    
    carros = list(portfolio.keys())
    
    if not portfolio:
        print('\nTodos os carros estão alugados no momento!')
    else:
        for i, carro in enumerate(carros):
            print(f'[{i}] {carro} - R${portfolio[carro]} /dia')
    
    return carros
    

def alugar_carro():
    print('\n[ ALUGAR ] Dê uma olhada em nosso portfólio')
    
    if not portfolio:
        print('\nTodos os carros estão alugados no momento!')
    
    carros = mostrar_portfolio()
    
    while True:
        codigo_carro = input('Escolha o código do carro:\n')
        if codigo_carro.isdigit() and 0 <= int(codigo_carro) < len(carros):
            codigo_carro = int(codigo_carro)
            break
        print('Código inválido. Tente novamente!')
        
    carro_escolhido = carros[codigo_carro]
    
    while True:
        quantidade_dias_aluguel = int(input('Escolha por quantos dias deseja alugar:\n'))  
        
        if quantidade_dias_aluguel > 0:
            quantidade_dias_aluguel = quantidade_dias_aluguel
            break
        print('Número de dias inválido. Tente novamente.\n')
    

    preco_diario = portfolio[carro_escolhido]
    custo_total = quantidade_dias_aluguel * preco_diario
    
    while True:
        print(f'\nVocê escolheu {carro_escolhido} por {quantidade_dias_aluguel} dias.')
        print(f'O aluguel totalizaria R$ {custo_total}. Deseja alugar?\n')
        
        confirmar = int(input('0 - SIM | 1 - NÃO'))

        
        # Implementar estrutura de escolha do usuário se ele deseja alugar ou não
        
        print(f'Parabéns você alugou o {carro_escolhido} por {quantidade_dias_aluguel} dias.')
        
        # Implementar CONTINUAR ou SAIR
        # Implementar repetição caso o usuário informe um ID de carro inválido
        
        # Ao alugar o carro, ele tem que sumir da lista de carros para aluguel
        # Ao aalugar o carro, ele tem que ser adiiconado a uma lista de carros alugados

def devolver_carro():
    print('\nSegue a lista de carros alugados. Qual você deseja devolver?')
          
    # 



def main():
    menu_inicial()
    
    alugar_carro()
    
main()
    