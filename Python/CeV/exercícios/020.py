import random

a=input('Aluno 1: ')
b=input('Aluno 2: ')
c=input('aluno 3: ')
d=input('Aluno 4: ')
l=[a,b,c,d]
random.shuffle(l)
print('A ordem de apresentação será {}.'.format(l))