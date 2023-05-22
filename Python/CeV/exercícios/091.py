from time import sleep
from random import randint
from operator import itemgetter
dado = {}
for c in range(1,5):
    dado[f'Jogador {c}'] = randint(1,6)
ranking = []
print('Valores sorteados: ')
for k, v in dado.items():
    print(f'{k} tirou o número {v}')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse = True)
print('\033[1m-='*20)
print(f'{"RANKING DOS JOGADORES":^40}')
print('-=\033[m'*20)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com o número {v[1]}')
    sleep(1)
