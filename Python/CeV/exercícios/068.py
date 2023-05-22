from random import randint
v = 0
print('=+'*20)
print('            PAR OU ÍMPAR?')
print('=+'*20)

while True:
    n = int(input('Digite um número: '))
    p = str(input('Par ou Ímpar? [P/I] ')).upper()
    print('-' * 50)
    c = randint(0 , 10)
    s = n + c
    v += 1
    if s % 2 == 0:
        print(f'Você escolheu {n} e o computador {c}. A soma deu {s} e é PAR')
        print('-'*50)
        if p == 'P':
            print('\033[1;32mVocê ganhou!\033[m')
        if p == 'I':
            print('\033[1;31mVocê perdeu!\033[m')
            break
    if s % 2 == 1:
        print(f'Você escolheu {n} e o computador {c}. A soma deu {s} e é ÍMPAR')
        if p == 'I':
            print('\033[1;32mVocê Ganhou!\033[m')
        if p == 'P':
            print('\033[1;31mVocê perdeu!\033[m')
            break
print(f'Você ganhou \033[1;36m{v - 1}\033[m vezes seguidas. Tente novamente!')