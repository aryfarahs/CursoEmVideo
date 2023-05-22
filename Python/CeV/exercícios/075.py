a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Mais um: '))
d = int(input('Último: '))

e = a, b, c, d
print('Você digitou os números: ' , end='')
for num in e:
    print(f'{num}' , end= ', ')
print(f'\nO número 9 aparece {e.count(9)} vez(es).')
if 3 in e:
    print(f'O número 3 aparece primeiramente na posição {e.index(3)+1}.')
else:
    print(f'O número 3 não aparece.')
print(f'Os números pares foram:', end=' ')
for n in e:
    if n % 2 == 0:
        print(n , end=', ')