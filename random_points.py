import random
while True:
    ds = input('Testar dnv? (S/N): ')
    if ds == 'S':
        pa = 0
        pb = 0
        empates = 0

        while pa <10000 and pb < 10000:
            a = random.randint(1, 2)
            b = random.randint(1, 2)

            if a == b:
                empates += 1
            elif a > b:
                pa += 1
            elif b > a:
                pb += 1

        print(f'{pa}, {pb}, empates: {empates}')
    else:
        break