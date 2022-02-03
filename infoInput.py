nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
altura = input('Qual a sua altura? ')
peso = input('Qual é o seu peso? ')
imc = float(peso) / float(altura) ** 2
ano_atual = 2021
nascimento = ano_atual - int(idade)
print()
print(f'{nome} tem {idade} anos de idade, {altura} de altura e pesa {peso}kg')
print(f'{nome} nasceu em {nascimento}, e seu IMC é de {imc:.2f} ')
