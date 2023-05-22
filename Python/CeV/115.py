from UTEIS import menu, math, titulo, linha
from time import sleep
from UTEIS.arquivo import *

arq = 'ex115.txt'
if arqExiste(arq):
    print(f'Analisando arquivo {arq}...')
else:
    criarArquivo(arq)

menu(['Realizar cadastro', 'Lista de cadastrados', 'Encerrar programa'])
while True:
    choice = math.leiaInt('\033[1;36mO que deseja fazer? \033[m')
    if choice == 1:
        titulo('Realizar Cadastro')
        nome = str(input('Nome: '))
        idade = math.leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print(linha())
    elif choice == 2:
        leiaArquivo(arq)
        print(linha())
    elif choice == 3:
        titulo('Obrigado pela preferência. Até a próxima!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    sleep(1)