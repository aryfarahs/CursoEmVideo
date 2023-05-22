l = list()
while True:
    n = int(input('Digite um número: '))
    if n not in l:
        l.append(n)
    else:
        print('\033[1;31mEsse número já foi digitado!\033[m')
    d = str(input('Deseja continuar? [S/N] ')).upper()
    if d == 'N':
        break
print('-'*40)
print(f'Você digitou os números {l}')
print('-'*40)
print(f'Nessa lista, existem {len(l)} números.')
l.sort(reverse=True)
print(f'Em ordem decrescente ela fica assim: {l}')
if 5 in l:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado')