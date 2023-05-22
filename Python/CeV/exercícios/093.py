jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantos jogos {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for v, k in jogador.items():
    print(f'O campo {v} tem valor {k}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    -Na {i+1}ª partida fez {v} gols.')
print(f'No total foram {jogador["total"]} gols.')