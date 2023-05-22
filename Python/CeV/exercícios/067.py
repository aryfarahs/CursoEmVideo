print('='*20)
print('Gerador de Tabuada')
print('='*20)
while True:
    n = int(input('Qual número deseja ver a tabuada? '))
    print('-'*20)
    if n < 0:
        break
    for t in range(1 , 11):
        print(f'{n} x {t} =' , t * n)
    print('-'*20)
print('='*20)
print('Progama encerrado. Volte sempre!')