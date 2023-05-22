print('-=' * 20)
print(' '*12 , 'Gerador de PA')
print('-=' * 20)
a1 = int(input('Primeiro valor: '))
r = int(input('A razão da PA: '))
n = a1
c = 1
tot = 0
aX = 5

while aX != 0:
    tot += aX
    while c <= tot:
        print(f'{n} ->' , end=' ')
        n += r
        c += 1
    print('PAUSA')
    aX = int(input('Quantos mais termos quer saber? '))
print('FIM')