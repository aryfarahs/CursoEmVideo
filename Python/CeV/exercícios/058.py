from random import randint
c = randint(0 , 10)
acertou = False
palpites = 0

print('O computador pensou em um número de 1 a 10. Tente adivinhar!')
while not acertou:
    j = int(input('Digite é seu palpite: '))
    palpites += 1
    if j == c:
        acertou = True
    else:
        if j > c:
            print('Menos...')
        elif j < c:
            print('Mais...')
print(f'Parabéns! Depois de \033[1;36m{palpites}\033[m tentativas você acertou!')