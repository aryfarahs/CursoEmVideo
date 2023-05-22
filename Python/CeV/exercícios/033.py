print('Pense em três números e digite;')
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

if a>b and a>c:
    print(f'{a} é o MAIOR número.')
if b>a and b>c:
    print(f'{b} é o MAIOR número.')
if c>a and c>b:
    print(f'{c} é o MAIOR número.')

if a<b and a<c:
    print(f'{a} é o MENOR número.')
if b<a and b<c:
    print(f'{b} é o MENOR número.')
if c<a and c<b:
    print(f'{c} é o MENOR número.')