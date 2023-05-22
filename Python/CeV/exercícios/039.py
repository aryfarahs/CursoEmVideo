from datetime import date
n = int(input('Bom dia. Qual o ano do seu nascimento? '))
a = date.today().year
i = a - n
d = i - 18

if i>18:
    print(f'Com {i} anos já realizou seu alistamento militar, certo? É para ter sido feito há \033[1;31m{d}\033[m ano(s)!')
    m = a - d
    print(f'No ano de \033[1;36m{m}')

elif i<18:
    print(f'{i} anos? Se prepare! Seu alistamento militar será daqui \033[1;31m{d * -1}\033[m ano(s).')
    m = a - d
    print(f'No ano de \033[1;36m{m}')

else:
    print(f'Está preparado? Seu alistamento militar será \033[1;31mneste ano!')