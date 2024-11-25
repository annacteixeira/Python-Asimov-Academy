import random

capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

estados = list(capitais.keys())
random.shuffle(estados)

acertos = 0
total = 0

print('=' * 80)
print('Seja bem-vindo ao jogo dos Estados!')
print('Você precisa responder o nome da capital de cada estado do Brasil.')
print('=' * 80)

for estado in estados:
    resposta = input(f"Qual a capital do estado {estado}? ").strip()
    if resposta.lower() == capitais[estado].lower():
        print("Resposta correta!")
        acertos += 1
    else:
        print(f"Resposta errada! A capital de {estado} é {capitais[estado]}.")
    
    total += 1
    
    continuar = input("Você deseja continuar? [S/N]: ").strip().lower()
    if continuar == 'n':
        break

print('=' * 80)
print(f"Você respondeu {total} perguntas.")
print(f"Acertos: {acertos}")
print(f"Porcentagem de acertos: {acertos / total * 100:.2f}%")
print("Obrigada por jogar!")
print('=' * 80)