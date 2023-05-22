from random import randint

a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
d = randint(1,10)
e = randint(1,10)

comp = a, b, c, d, e
print(f'Os números sorteados foram:', end=' ')
for n in comp:
    print(f'{n}' , end=' ')
print(f'\nO \033[1;32mmaior\033[m valor é: {max(comp)}')
print(f'O \033[1;31mmenor\033[m valor é: {min(comp)}')