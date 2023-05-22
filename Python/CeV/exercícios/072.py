ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n1 = int(input('Digite um número de 0 a 20: '))
if 0 > n1 or n1 > 20:
    while True:
        n1 = int(input('Tente novamente. Digite um número de 0 a 20: '))
        if 0 < n1 < 20:
            break

c = ext[n1]
print(f'Esse número por extenso se escreve {c}')