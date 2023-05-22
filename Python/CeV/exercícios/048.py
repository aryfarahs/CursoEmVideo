soma = 0
cont = 0
for a in range(1 , 500):
    if a % 2 == 1 and a % 3 == 0:
        soma = soma + a
        cont = cont + 1
print(f'Existem {cont} números solicitados. A soma entre eles é {soma}.')
