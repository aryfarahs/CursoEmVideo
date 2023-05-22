n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('E a sua segunda? '))
n3 = (n1 + n2) / 2

print(f'A média entre {n1} e {n2} é de \033[4m{n3:.1f}.')

if n3 >= 7.0:
    print('Você está \033[1;4;32mAPROVADO!')

elif 3.0 < n3 < 7.0:
    print('Você está de \033[1;4;33mRECUPERAÇÃO!')

else:
    print('Você está \033[1;4;31mREPROVADO!')