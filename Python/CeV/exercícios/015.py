d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos km foram rodados? '))
print('O preço do aluguel será de R${:.2f}.'.format((d*60)+(0.15*k)))
