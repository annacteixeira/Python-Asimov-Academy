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
    
    opcao_menu = int(input('O que deseja fazer?\n0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro | 3 - Sair\n'))
    return opcao_menu 

def mostrar_portfolio(portfolio_atual):
    if not portfolio_atual:
        print('\nTodos os carros estão alugados no momento!')
        return []
    
    carros = list(portfolio_atual.keys())

    for i, carro in enumerate(carros):
        print(f'[{i}] {carro} - R${portfolio_atual[carro]} /dia')
        
    return carros

def alugar_carro():
    global portfolio, carros_alugados
    
    if not portfolio:
        print('\nTodos os carros estão alugados no momento!')
        return
    
    print('\n[ ALUGAR ] Dê uma olhada em nosso portfólio')
    
    carros = mostrar_portfolio(portfolio)
    
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
            break
        print('Número de dias inválido. Tente novamente.\n')
    
    preco_diario = portfolio[carro_escolhido]
    custo_total = quantidade_dias_aluguel * preco_diario
    
    while True:
        print(f'\nVocê escolheu {carro_escolhido} por {quantidade_dias_aluguel} dias.')
        print(f'O aluguel totalizaria R$ {custo_total}. Deseja alugar?\n')
        
        confirmar = int(input('0 - SIM | 1 - NÃO\n'))
        
        if confirmar in [0, 1]:
            break
        print('\nEntrada inválida. Digite [0] para sim ou [1] para não')
    
    if confirmar == 0:
        carros_alugados[carro_escolhido] = preco_diario
        del portfolio[carro_escolhido]
        print(f'Parabéns você alugou o {carro_escolhido} por {quantidade_dias_aluguel} dias.')
    else:
        print('\nAluguel cancelado.')

def devolver_carro():
    global portfolio, carros_alugados
    
    if not carros_alugados:
        print('\nNão há carros alugados no momento.')
        return
    
    carros = list(carros_alugados.keys())
    print('\nSegue a lista de carros alugados. Qual você deseja devolver?')
    
    for i, carro in enumerate(carros):
        print(f'[{i}] {carro} - R${carros_alugados[carro]} /dia')
    
    while True:
        carro_devolver = input('\nEscolha o código do carro que deseja devolver:\n')
        if carro_devolver.isdigit() and 0 <= int(carro_devolver) < len(carros):
            carro_devolver = int(carro_devolver)
            break
        print("Código inválido. Tente novamente.")
    
    carro_devolvido = carros[carro_devolver]
    portfolio[carro_devolvido] = carros_alugados.pop(carro_devolvido)
    print(f'\nObrigado por devolver o carro {carro_devolvido}.')

def main():
    while True:
        opcao = menu_inicial()
        if opcao == 0:
            mostrar_portfolio(portfolio)
        elif opcao == 1:
            alugar_carro()
        elif opcao == 2:
            devolver_carro()
        elif opcao == 3:
            print('\nAté mais...')
            break
        else:
            print('\nOpção inválida!\n')
            
main()