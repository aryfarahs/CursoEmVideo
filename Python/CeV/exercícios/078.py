val = []
mai = men = 0
for num in range(0,5):
    val.append(int(input(f'Digite um número para a posição {num}: ')))
    if num == 0:
        mai = men = val[num]
    else:
        if val[num] > mai:
            mai = val[num]
        if val[num] < men:
            men = val[num]

print(f'Você digitou os números {val}')
print(f'O maior valor digitado foi {mai} e está nas posições ', end='')
for i, v in enumerate(val):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} e está nas posições ', end='')
for i, v in enumerate(val):
    if v == men:
        print(f'{i}...', end=' ')


