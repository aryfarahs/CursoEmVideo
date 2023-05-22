f = list()
tot = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    f.append([nome , [n1 , n2] , media])
    a = str(input('Deseja continuar? [S/N] ')).upper()
    tot += 1
    if a == 'N':
        break
media = (n1 + n2) % 2
print('-'*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*20)
for i, l in enumerate(f):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar a nota de qual aluno? (999 ENCERRA)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(f) - 1:
        print(f'As notas do aluno {f[opc][0]} são {f[opc][1]}')
print('VOLTE SEMPRE!')

