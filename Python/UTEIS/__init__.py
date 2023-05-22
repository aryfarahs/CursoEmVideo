from UTEIS import math
def linha(qnt=40):
    return '—' * qnt


def menu(x):
    titulo('CADASTRO')
    c = 1
    for item in x:
        print(f'\033[1;36m{c} -\033[m {item}')
        c += 1
    print(linha())


def titulo(msg):
    print(f'{"—" * 40}')
    print(f'{msg:^40}')
    print(f'{"—" * 40}')