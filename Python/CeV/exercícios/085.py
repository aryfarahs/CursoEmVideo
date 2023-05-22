m = n =0
l = [[] , []]

for c in range(0, 7):
    m += 1
    n = int(input(f'Digite o {m}° valor: '))
    if n % 2 == 0:
         l[0].append(n)
    if n % 2 == 1:
        l[1].append(n)
l[0].sort()
l[1].sort()
print(f'Os números pares são {l[0]}')
print(f'Os números ímpares são {l[1]}')