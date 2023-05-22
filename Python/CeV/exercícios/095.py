jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    tot = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantidade de gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responda somente S ou N')
    if resp in 'N':
        break
print('-'*40)
print("cod ", end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
print('-'*40)
while True:
    busca = int(input('Qual jogador deseja visualizar? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe um jogador com código {busca}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

