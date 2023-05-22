print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)

n = int(input('Quanto números da sequência deseja ver? '))
n1 = 0
n2 = 1
c = 3

print(f'\n{n1} -> {n2} -> ' , end='')

while c <= n:
    n3 = n1 + n2
    c += 1
    print(f'{n3} ->' , end=' ')
    n1 = n2
    n2 = n3
print('FIM')