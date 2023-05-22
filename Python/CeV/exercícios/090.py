aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('\033[1m-=\033[m'*20)
print(f'O aluno {aluno["nome"]} teve a média {aluno["media"]}')
if aluno['media'] < 5:
    print('Situação: \033[1;4;31mREPROVADO\033[m')
elif 5 <= aluno['media'] < 7:
    print('Situação: \033[1;4;33mRECUPERAÇÃO\033[m')
elif aluno['media'] >= 7:
    print('Situação: \033[1;4;32mAPROVADO\033[m')
else:
    print('MÉDIA INEXISTENTE. Tente novamente')