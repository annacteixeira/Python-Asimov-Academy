# n é o parâmetro da função
def somar_dois(n):
    return n + 2

x = 10

# x é o argumento que passamos para a função
resultado = somar_dois(x)
print(resultado)

# O valor 'final' pode ser especificado ou omitido. Caso seja omitido, será o valor declarado na função
def adicionar_final(texto, final ='!!!'):
    return texto + final

print(adicionar_final('Olá'))

def dividir(a, b):
    if b == 0:
        return 'Impossível dividir'

    return a / b
    
print(dividir(10, 5))
# >> 2.0

# OU
print(dividir(a = 10, b = 5))
# >> 2.0

print(dividir(a = 10, b = 0))
# >> Impossível dividir

print(dividir(b = 10, a = 0))
# >> 0.0

def dizer_ola():
    print('Olá')
    
dizer_ola()
# >> Olá