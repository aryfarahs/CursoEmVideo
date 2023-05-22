soma = 0
print('ECOLHA 6 NÚMEROS')
for n in range(0 , 6):
    i = int(input('Digite: '))
    if i % 2 == 0:
        soma = soma + i
print(f'A soma entre os números pares é {soma}')