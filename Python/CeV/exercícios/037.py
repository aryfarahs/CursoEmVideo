n = int(input('Digite um número inteiro qualquer: '))

print('\033[4;33m[ 1 ] BINÁRIO \n\033[4;34m[ 2 ] OCTAL \n\033[4;35m[ 3 ] HEXADECIMAL \n\033[m')

o = int(input('\033[7mSELECIONE UMA OPÇÃO:\033[m '))

if o == 1:
    print(f'O número {n} em \033[1;36mBINÁRIO\033[m é: {bin(n) [2:]}')

elif o == 2:
    print(f'O número {n} em \033[1;36mOCTAL\033[m é: {oct(n) [2:]}')

elif o == 3:
    print(f'O número {n} em \033[1;36mHEXADECIMAL\033[m é: {hex(n) [2:]}')

else:
    print('\033[4;30;41mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')