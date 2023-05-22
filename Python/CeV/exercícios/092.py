from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de Nascimento: '))
dados['Ctps'] = int(input('Carteira de Trabalho [0 se inexistente]: '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário (R$): '))
    dados['Aposentadoria'] = ((dados['Contratação'] + 35) - datetime.now().year)
print('-='*30)
for v, k in dados.items():
    print(f'\033[1;4m-{v}:\033[m {k}')
