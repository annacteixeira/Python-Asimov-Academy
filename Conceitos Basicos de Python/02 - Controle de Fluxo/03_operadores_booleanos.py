# Os operadores booleanos são:
    # and
    # or
    # not
    
print(True and True)
# >> True

print(True and False)
# >> False

print(False and False)
# >> False

print(True or True)
# >> True

print(True or False)
# >> True

print(False or False)
# >> False

print(not True)
# >> False

print(not False)
# >> True

print('------ INÍCIO ------\n')

estou_com_fome = input('Estou com fome? Digite s para sim: ') == 's'
tenho_comida = input('\nTenho comida em casa? Digite s para sim: ') == 's'


if estou_com_fome and not tenho_comida:
    print('\nIr ao mercado')
    print('\nVoltar para casa')
    print('\nPreparar uma refeição')
    print('\nComer a comida')
    
if estou_com_fome and tenho_comida:
    print('\nPreparar uma refeição')
    print('\nComer a comida')

print('\n----- FIM -----\n')