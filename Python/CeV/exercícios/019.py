import random
a=input('Primeiro aluno: ')
b=input('Segundo aluno: ')
c=input('Terceiro aluno: ')
d=input('Quarto aluno: ')
l=[a,b,c,d]
print('O sorteado foi {}!'.format(random.choice(l)))