nome = 'Paulo'
idade = 16
altura = 1.63
peso = 56.5
ano_atual = 2021
imc = peso / (altura ** 2)
nascimento = ano_atual - idade
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')