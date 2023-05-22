from random import randint
from time import sleep
r=randint(0,5)
print('-' * 55)
print('Vou pensar em um números entre 0 e 5, tente adivinhar.')
print('-' * 55)
j = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
print('Parabéns, você acertou!') if j == r else print('Que pena, você errou.')
print(f'Pensei no número: {r}')
