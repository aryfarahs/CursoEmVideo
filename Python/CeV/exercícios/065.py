o = 'S'
s = q = média = maior = menor = 0
while o == 'S':
    n = int(input('Digite um número: '))
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    o = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = s/q
print(f'A média entre esses {q} valores é: {média}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')