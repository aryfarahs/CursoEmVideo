j = int(input('Qual é a velocidade do carro? '))
if j <= 75:
    print('Tudo certo, boa viagem!')
if 75 < j <= 80:
    print('CUIDADO! O limite permitido é 80km/h')
if j > 80:
    multa = (j-80) * 7
    print(f'O limite de velocidade foi atingido, você terá que pagar uma multa de R${multa:.2f}')