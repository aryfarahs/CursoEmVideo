pal = ('Gabinete', 'Teclado', 'Mouse', 'Monitor', 'Led')

for vog in pal:
    print(f'\nA palavra {vog} tem as vogais', end=' ')
    for letra in vog:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
