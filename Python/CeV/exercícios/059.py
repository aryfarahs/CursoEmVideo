p1 = int(input('\033[1mPrimeiro valor: '))
p2 = int(input('Segundo valor: \033[m'))
n = 0

while n != 5:
    print('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa')
    n = int(input('\033[1mO que deseja fazer? \033[m'))
    if n == 1:
        print(f'A \033[1;34msoma\033[m entre \033[1;35m{p1}\033[m e \033[1;35m{p2}\033[m é\033[1;34m {p1 + p2}\033[m \n' , '\033[1m-=\033[m'*15)
    elif n == 2:
        print(f'A \033[1;33mmultiplicação\033[m entre \033[1;36m{p1}\033[m e \033[1;36m{p2}\033[m é \033[1;33m{p1 * p2}\033[m \n', '\033[1m-=\033[m'*15)
    elif n == 3:
        if p1 > p2:
            print(f'O \033[1;31mmaior\033[m desses números é \033[1;31m{p1}\033[m\n' , '\033[1m-=\033[m'*15)
        else:
            print(f'O \033[1;31mmaior\033[m desses números é \033[1;31m{p2}\033[m\n' , '\033[1m-=\033[m'*15)
    elif n == 4:
        print('\033[1m-=\033[m'*15)
        p1 = int(input('\033[1mPrimeiro valor: '))
        p2 = int(input('Segundo valor: \033[m'))
print('\033[7mFoi um prazer te ajudar!\033[m')