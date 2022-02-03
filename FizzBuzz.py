a = int(input('N1: '))
def qq(a):
    if not a % 15:
        print('FizzBuzz')
    elif not a % 3:
        print('fizz')
    elif not a % 5:
        print('buzz')
    else:
        print(a)

qq(a)