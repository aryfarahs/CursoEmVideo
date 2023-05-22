t = q = mn = c = 0
print('-'*40)
print('{: ^40}'.format('ATACADÃO DO ARY'))
print('-'*40)
while True:
    n = str(input('Qual o nome do produto? '))
    p = int(input('Qual o preço? [R$] '))
    d = str(input('Deseja continuar? [S/N] ')).upper()
    t += p
    c += 1
    if c == 1:
        mn = p
    else:
        if p < mn:
            mn = p
    if p > 1000:
        q += 1
    if d == 'N':
        break
print('-'*30)
print(f'O total gasto na compra foi \033[1;35m{t}\033[m;\n\033[1;31m{q}\033[m produtos custam mais de R$1000,00;'
      f'\nO produto mais barato custou \033[1;34mR${mn:.2f}\033[m.')