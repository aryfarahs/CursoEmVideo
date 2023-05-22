n = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in n:
        n.append(v)
        print(f'Número {v} adicionado com sucesso!')
    else:
        print(f'O número {v} já foi adicionado! Tente novamente.')
    c = str(input('Deseja continuar? [S/N] ')).upper()
    if c == 'N':
        break
print('-'*50)
n.sort()
print(f'Você digitou os valores: {n}')
