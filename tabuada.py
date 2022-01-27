resposta = input('Vc deseja ver a tabuada de qual numero?: ')
resposta = int(resposta)
li10 = list(range(0,11))
print('-----------------')
for n in li10:
    print(f'{resposta} * {n} = {resposta * n}')
    
print('-----------------')
