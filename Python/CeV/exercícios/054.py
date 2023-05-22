from datetime import date

atual = date.today().year
tmaior = 0
tmenor = 0

for n in range(1 , 8):
    a = int(input(f'Em que ano a {n}° pessoa nasceu? '))
    i = atual - a
    if i >= 18:
        tmaior += 1
    else:
        tmenor += 1

print(f'Existem {tmaior} pessoas maiores de idade.')
print(f'Existem {tmenor} pessoas menores de idade.')