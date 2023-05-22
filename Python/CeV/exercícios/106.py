color = ('\033[1;40m',     # 0 - Preto
         '\033[1;30;41m',  # 1 - Vermelo
         '\033[1;30;42m',  # 2 - Verde
         '\033[1;30;43m',  # 3 - Amarelo
         '\033[1;30;44m',  # 4 - Lilás
         '\033[1;30;45m',  # 5 - Rosa
         '\033[1;30;46m',  # 6 - Ciano
         '\033[1;30;47m',  # 7 - Cinza
         )
def ajuda(com):
    help(com)

cor = int(input('Qual cor deseja? '))
while True:
    print(f'{color[cor]}–' * 40, '\033[m')
    print(f'{color[cor]}{"CENTRAL DE AJUDA":^40}', '\033[m')
    print(f'{color[cor]}–' * 40, '\033[m')
    c = str(input('Forneça o comando -> ')).lower()
    if c.upper() == 'FIM':
        break
    else:
        ajuda(c)
print('Obrigado pela preferência!')