# Dadas duas listas, printe todos os valores que aparecerem duplicados nas duas listas.
print('-' * 100)

palavras_01 = ['abacate', 'banana', 'cereja', 'damasco', 'jaca', 'laranja']
palavras_02 = ['abacate', 'acerola', 'damasco', 'laranja', 'kiwi', 'limão']

for palavra_01 in palavras_01:
    for palavra_02 in palavras_02:
        if palavra_01 == palavra_02:
            print(palavra_01)

print('-' * 100)

# Dadas duas listas, printe uma mensagem dizendo se existe algum elemento comum entre elas ou não.
compras = ['frango', 'carne', 'suco', 'chocolate', 'salgadinho', 'laranja']
geladeira = ['uva', 'frango', 'carne', 'água', 'refrigerante', 'feijão']

contador = 0

for compra in compras:
    for alimento in geladeira:
        if compra == alimento:
            contador += 1
            
if contador >= 1:
    print(f'\nAs listas possuem {contador} elementos em comum\n')
else:
    print('\nAs listas não possuem elementos em comum\n')