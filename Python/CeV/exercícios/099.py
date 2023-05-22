#l = []
#while True:
#    n = int(input('Digite um número [999 p/ parar]: '))
#    if n == 999:
#        break
#    if n not in l:
#        l.append(n)
#    else:
#        print('\033[1;4mEsse número já foi adicionado!\033[m')
#for i,v in enumerate(l):
#    print(f'{v }', end='')
from time import sleep

def maior( * num):
    cont = maior = 0
    print('~' * 30)
    print('\nAnalizando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam oferecidos \033[1;4m{len(num)}\033[m valores')
    print(f'O maior valor entre eles é \033[1;4m{maior}\033[m')


maior(2, 34, 5, 7, 3, 11)
maior(423)