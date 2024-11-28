import math
import datetime
import random
import os
import time

# ==========================================================================================
# Módulo math

print(math.pi)
# >> 3.141592653589793

print(math.log(16,2))
# >> 4.0

print('\n')

# ==========================================================================================
# Módulo datetime

print(datetime.datetime.now())
# >> 2024-11-25 15:58:14.747047

agora = datetime.datetime.now()
ano_2000 = datetime.datetime(2000, 1, 1)

print(agora - ano_2000)
# >> 9095 days, 15:59:25.991625

print('\n')
# ==========================================================================================
# Módulo random

for _ in range(10):
    n = random.randint(1, 10)
    print(f'Número escolhido: {n}')
    
nomes = ['Juliano', 'Marcos', 'Paulo']

for _ in range(5):
    nome = random.choice(nomes)
    print(f'Nome escolhido: {nome}')

print('\n')
# ==========================================================================================
# Módulo os (operating system)

print(os.getcwd())
# >> C:\Users\annaf\Documentos\Anna\Asimov Academy\Python-Asimov-Academy

print(os.listdir())
# >> C:\Users\annaf\Documentos\Anna\Asimov Academy\Python-Asimov-Academy

print('\n')
# ==========================================================================================
# Módulo time

inicio = time.time()
print('Primeira linha')

time.sleep(1)

print('Segunda linha')

final = time.time()

tempo_execucao = final - inicio

print(f'O script levou {tempo_execucao:.3f} segundos para executar')