from random import randint
from time import sleep

print('='*20)
print('\033[44;1;30mPEDRA, PAPEL OU TESOURA!\033[m')
print('='*20)
print('[ 1 ] PEDRA \n[ 2 ] PAPEL \n[ 3 ] TESOURA')

j = int(input('Escola sua jogada: '))
r = randint(1,3)

print('JO... ' , end=""); sleep(1); print('KEN... ' , end=""),; sleep(1); print('PÔ!!!')

print('-'*15)
if j == 1:
    print('JOGADOR ESCOLHEU PEDRA')
elif j == 2:
    print('JOGADOR ESCOLHEU PAPEL')
elif j == 3:
    print('JOGADOR ESCOLHEU TESOURA')

if r == 1:
    print('MÁQUINA ESCOLHEU PEDRA')
elif r == 2:
    print('MÁQUINA ESCOLHEU PAPEL')
elif r == 3:
    print('MÁQUINA ESCOLHEU TESOURA')
print('-' * 15)

if r == j:
    print('O jogo terminou em \033[1;33mEMPATE!')

elif r == 1 and j == 2:
    print('Você \033[1;32mVENCEU!')
elif r == 1 and j == 3:
    print('Você \033[1;31mPERDEU')

elif r == 2 and j == 1:
    print('Você \033[1;31mPERDEU!')
elif r == 2 and j == 3:
    print('Você \033[1;32mVENCEU!')

elif r == 3 and j == 1:
    print('Você \033[1;32mVENCEU!')
elif r == 3 and j == 2:
    print('Você \033[1;31mPERDEU')