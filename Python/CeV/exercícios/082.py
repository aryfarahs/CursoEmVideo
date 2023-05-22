l = list()
p = []
i = []
while True:
    n = int(input('Digite um valor: '))
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    c = str(input('Deseja continuar? [S/N] ')).upper()
    if c == 'N':
        break
print(f'Os Valores digitados em ordem crescente foram: {sorted(l)}')
print(f'Os números pares são {sorted(p)}')
print(f'Os números ímpares são {sorted(i)}')

