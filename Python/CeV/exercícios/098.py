from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM')


#PROGRAMA PRINCIPAL
print('=-'*30)
contador(1, 10, 1)
print('=-'*30)
contador(10, 0, 2)
print('=-'*30)
print('Agora é sua vez de decidir!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
