user = input('Seu usuario: ')
try:
    tam_user = len(user)

    if tam_user >= 5 and tam_user <= 6:
        print('Seu nome é normal :)')
    elif tam_user < 5:
        print('Seu nome é curto :(')
    elif tam_user > 6:
        print('Seu nome é muito grande :(')
except:
    print('Erro')