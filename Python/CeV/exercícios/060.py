from math import factorial

n = int(input('Digite um número inteiro: '))
f = factorial(n)
c = n

while c > 0:
    print(f'{c}', end='')
    print(' • ' if c > 1 else f' = {f}' , end='')
    c -= 1
print(f'\nEntão {n}! = {f}.')
