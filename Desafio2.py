hora = input('Querido humano, que horas sao?: ')
try:
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 24:
        print('Boa noite')
    elif hora < 0 or hora > 24:
        print('Erro. Digite um numero entre 0 e 24')
    else:
        print('Erro')

except:
    print('Erro, digite a hora, e SOMENTE ELA. Ex: 23')