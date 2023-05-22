r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    if r1 != r2 != r3:
        print('Com essas retas, \033[1;34mÉ POSSÍVEL\033[m formar um triangulo \033[1;33mESCALENO.')
    elif r1 == r2 == r3:
        print('Com essas retas, \033[1;34mÉ POSSÍVEL\033[m formar um triangulo \033[1;36mEQUILÁTERO.')
    else:
        print('Com essas retas, \033[1;34mÉ POSSÍVEL\033[m formar um triangulo \033[1;31mISÓSCELES.')

else:
    print('\033[4;7;31;40mNão é possível formar um triângulo com essas retas.\033[m')
