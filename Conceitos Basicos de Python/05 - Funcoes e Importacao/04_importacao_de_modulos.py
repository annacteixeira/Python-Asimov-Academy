import meu_modulo

retorno = meu_modulo.minha_funcao()

print(retorno)
print(meu_modulo.x)

print('\n')

# OU

from meu_modulo import minha_funcao, x

retorno = minha_funcao()
print(retorno)
print(x)

# OU

# Importa tudo que está dentro do módulo
from meu_modulo import *

# OU
print('\n')
# Dando um alias para o módulo

import meu_modulo as mm

retorno = mm.minha_funcao()
print(retorno)
print(x)

# Importando partes específicas do módulo com alias
print('\n')
from meu_modulo import minha_funcao as mf, x as X

retorno = mf()
print(retorno)
print(X)
