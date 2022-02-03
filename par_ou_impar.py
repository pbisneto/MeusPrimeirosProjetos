p1 = input('Digite um numero inteiro: ')
p2 = p1
try:
    p2 = int(p2)
    if p2 % 2 == 0:
        print(f'{p2} é par')
    else:
        print(f'{p2} é impar')
except:
    print('Este nao é um numero inteiro!')
