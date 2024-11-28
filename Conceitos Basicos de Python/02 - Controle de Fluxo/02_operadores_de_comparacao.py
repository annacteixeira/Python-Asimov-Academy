# Os operadores de comparação em Python são:

# > e < : maior e menor
# == : igual a
# >= e <= : maior ou igual e menor ou igual
# != : não igual / diferente

print(5 > 5)
# >> False

print (5 < 5)
# >> False

print (5 == 5)
# >> True

print(5 >= 5)
# >> True

print(5 <= 5)
# >> True

print('------ INÍCIO ------\n')
resposta1 = input('Estou com fome? Digite s para sim: ')

if resposta1 == 's':
    resposta2 = input('\nTenho comida em casa? Digite s para sim: ')

    if resposta2 != 's':
       print('\nIr ao mercado')
       print('\nVoltar para casa')
    print('\nPreparar uma refeição')
    print('\nComer a comida')
    

print('\n----- FIM -----\n')