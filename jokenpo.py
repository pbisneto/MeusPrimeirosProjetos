import random

while True:
    r = input('Deseja jogar jokenpo (S/N): ')
    if r == 'S':
        lista = ['R', 'P', 'S']
        pppc = 0
        ppus = 0

        while pppc < 3 and ppus < 3:


            resposta_user = input('R, P, S, ?')
            resposta_pc = random.choice(lista)
            res = (f'Pc {pppc}, User {ppus}')

            if resposta_user == resposta_pc:
                print(f'Empate! Ambos jogaram {resposta_user}')
                print(res)
            else:
                if resposta_user == 'R' and resposta_pc == 'P':
                    pppc = pppc + 1
                    print(f'Pc jogou {resposta_pc}')
                    print('Pc pontuou')
                    print(f'Pc {pppc}, User {ppus}')
                elif resposta_user == 'P' and resposta_pc == 'S':
                    pppc = pppc + 1
                    print(f'Pc jogou {resposta_pc}')
                    print('Pc pontuou')
                    print(f'Pc {pppc}, User {ppus}')
                elif resposta_user == 'S' and resposta_pc == 'R':
                    pppc = pppc + 1
                    print(f'Pc jogou {resposta_pc}')
                    print('Pc pontuou')
                    print(f'Pc {pppc}, User {ppus}')
                elif resposta_user == 'R' and resposta_pc == 'S':
                    ppus = ppus + 1
                    print(f'Pc jogou {resposta_pc}')
                    print('Voce pontuou')
                    print(f'Pc {pppc}, User {ppus}')
                elif resposta_user == 'P' and resposta_pc == 'R':
                    ppus = ppus + 1
                    print(f'Pc jogou {resposta_pc}')
                    print('Voce pontuou')
                    print(f'Pc {pppc}, User {ppus}')
                elif resposta_user == 'S' and resposta_pc == 'P':
                    ppus = ppus + 1
                    print(f'Pc jogou {resposta_pc}')
                    print('Voce pontuou')
                    print(f'Pc {pppc}, User {ppus}')

        if ppus == 3:
            print('Parabens! Voce ganhou em um jogo de sorte, logo, voce nao tem merito nenhum nisso :)')
        elif pppc == 3:
            print('Voce perdeu! Previsivel... hahaha')
    else:
        print('Quem luta, pode perder.')
        print('Quem não luta, já perdeu.')
        print('- Brecht')
        break
