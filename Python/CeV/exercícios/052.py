a1 = int(input('Digite o primeiro número de uma PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10 - 1) * r
print('Os 10 primeiros números dessa PA são:')

for n in range(a1 , a10 + r, r):
    print(f'{n}' , end=' -> ')
print('ACABOU!')