while True:
    ds = input('Deseja usar a calculadora? (S/N) ')
    if ds == 'S':
        n1 = input('Digite o primeiro numero: ')
        n2 = input('Digite o segundo numero: ')
        op = input('Digite o metodo de operacao: ')
        n1 = int(n1)
        n2 = int(n2)

        if op == '+':
            print(n1 + n2)
        elif op == '-':
            print(n1 - n2)
        elif op == '*':
            print(n1 * n2)
        elif op == '/':
            print(n1 / n2)
        else:
            print('Erro')
    elif ds == 'N':
        print('Obrigado pela preferencia! :)')
        break
    else:
        print('Erro')
