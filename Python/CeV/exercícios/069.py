p = h = m20 = 0
while True:
    n = str(input('Digite seu nome: '))
    s = str(input('Digite seu sexo [M/F]: ')).upper()
    i = int(input('Digite sua idade: '))
    c = str(input('Deseja continuar? [S/N] ')).upper()
    if i >= 18:
        p += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m20 += 1
    if c == 'N':
        break
print(f'\033[1;4mNesses cadastros:\033[m\n\033[1;36m{p}\033[m pessoas são maiores de 18 anos;\n\033[1;31m{h}\033[m são homens;\n\033[1;33m{m20}\033[m mulheres tem menos de 20 anos.')
