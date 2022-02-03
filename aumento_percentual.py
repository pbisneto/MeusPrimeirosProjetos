b = int(input('N1: '))
m = int(input('Porcentagem: '))

def fx(b, m):
    por = b / 100 * m
    sum = b + por
    print(f'{m}% de {b} = {por}, e a soma de {b} mais sua porcentagem ({por}) = {sum}')

fx(b, m)
