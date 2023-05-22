def score(j=0, g=0):
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if j != '':
        return f'O jogador {j} fez {g} gols. '
    else:
        return f'O jogador <desconhecido> fez {g} gols.'


jog = str(input('Nome do jogador: '))
gol = str(input('Quantidade de gols: '))
print(score(jog, gol))