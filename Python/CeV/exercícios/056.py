si = 0
m = 0
maiorh = 0
nvelho = 0
tmulher18 = 0

for p in range(1 , 5):
    print('-'*5 , f'{p}ª PESSOA' , '-'*5)
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    si += i
    if p == 1 and s in 'Mm':
        maiorh = i
        nvelho = n
    if s in 'Mm' and i > maiorh:
        maiorh = i
        nvelho = n
    if s in 'Ff' and i > 17:
        tmulher18 += 1



m = si / 4
print(f'A média das idades é de {m:.1f} anos')
print(f'O homem mais velho é {nvelho} e tem {maiorh} anos.')
print(f'Existem {tmulher18} mulheres maiores de idade.')