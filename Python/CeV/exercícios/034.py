s = int(input('Qual é o seu salário em R$? '))
a = 15/100 * s + s
m = 10/100 * s + s


if s>1250.00:
    print(f'Seu aumento será de 10%. Agora, passará a receber R${m:.2f}. ')
if s<=1250.00:
    print(f'Seu aumento será de 15%. Agora passará a receber R${a:.2f}.')