from random import randint
from time import sleep

def sorteia(num):
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        n = randint(1, 11)
        num.append(n)
        print(f'{n}', end=' ', flush= True)
        sleep(0.3)

def somaPar(num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares em {num} temos: {soma}')

print('–' * 40)
print(f'{"SORTEANDO NÚMEROS":^40}')
print('–' * 40)
l = []
sorteia(l)
somaPar(l)