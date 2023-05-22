lista = ('Lápis', 3.00,
         'Caderno', 10.50,
         'Borracha', 4.00,
         'Caneta', 7.30,
         'Penal', 16.00,
         'Mochila', 119.90,
         'Compasso', 12.00,
         'Transferidor', 14.90)
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)

for item in range(0 , len(lista)):
    if item % 2 ==0:
        print(f'{lista[item]:.<30}' , end='')
    else:
        print(f'R${lista[item]:>7.2f}')
print('-'*40)