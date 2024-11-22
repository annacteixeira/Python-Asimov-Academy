# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha
# - Se ambos forem corretos, exibe uma mensagem de sucesso
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
#   quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como variáveis dentro do código

usuario = 'usertest'
senha = 12345678

usuario_novo = input('Digite o usuário: ')
senha_nova = int(input('Digite a senha: '))

if usuario == usuario_novo and senha == senha_nova:
    print('Sucesso!')

elif usuario != usuario_novo and senha == senha_nova:
    print('Usuário inválido!')

elif usuario == usuario_novo and senha != senha_nova:
    print('Senha inválida!')

else:
    print('Usuário e senha inválidos!')