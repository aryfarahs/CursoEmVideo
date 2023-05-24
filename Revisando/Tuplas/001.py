t = ('zero', 'um', 'dois' ,'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenov', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    if n > 20 or n < 0:
        print('ERRO! Digite um valor válido.')
    else:
        break
print(f'O número {n} escrito por extenso é {t[n]}')