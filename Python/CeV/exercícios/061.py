a1 = int(input('Primeiro valor: '))
r = int(input('A razão da PA: '))
n = a1
c = 1

while c <= 10:
    print(f'{n} ->' , end=' ')
    n += r
    c += 1
print('FIM')