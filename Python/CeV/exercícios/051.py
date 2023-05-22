n = int(input('Digite um número para ver se ele é primo: '))
t = 0
for c in range(1 , n+1):
    if n % c == 0:
        print('\033[1;36m' , end=' ')
        t += 1
    else:
        print('\033[1;30m' , end=' ')
    print(f'{c}' , end=' ')
print(f'\n\033[mO número {n} pode ser dividido {t} vezes.')
if t > 2:
    print('Ele \033[31;1;4mnão\033[m é um número primo.')
else:
    print('Ele \033[32;1;4mé\033[m um número primo.')