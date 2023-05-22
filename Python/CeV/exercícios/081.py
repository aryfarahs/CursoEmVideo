l = []
for n in range(0, 5):
    v = int(input('Digite úm número: '))
    if n == 0 or v > l[-1]:
        l.append(v)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(l):
            if v <= l[pos]:
                l.insert(pos, v)
                break
            pos += 1
        print(f'Adicionando à posição {pos}')
print('-'*40)
print(f'Os valores digitados, em ordem crescente, foram: {l}')
print('-'*40)