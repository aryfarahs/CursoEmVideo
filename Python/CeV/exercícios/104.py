def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um valor válido\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um valor: ')
print(f'Você digitou o número {n}')