print('\033[35m-='*20 , '\n          COMPARADOR DE NÚMEROS\n' , '-=' *20 , '\033[m')

p = int(input('Primeiro número: '))
s = int(input('Segundo número: '))

if s>p:
    print('O \033[4;36mSEGUNDO\033[m é o maior número')
elif s<p:
    print('O \033[4;36mPRIMEIRO\033[m é o maior número')
else:
    print('Os dois números tem o \033[4;31mMESMO\033[m valor')
