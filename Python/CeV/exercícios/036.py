v = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o seu salário? R$'))
a = int(input('Em quantos anos pretende pagar? '))
p = v / (12 * a)

if p > 30/100 * s:

    print(f'\033[1mPara pagar uma casa de R${v:.2f} em {a} anos, a prestação será de R${p:.2f}')
    print('Empréstimo \033[1;31m NEGADO!\033[m')

elif p <= 30/100 * s:

    print(f'\033[1mPara pagar uma casa de R${v:.2f} em {a} anos, a prestação será de R${p:.2f}')
    print(f'Empréstimo \033[1;32m APROVADO!\033[m')
