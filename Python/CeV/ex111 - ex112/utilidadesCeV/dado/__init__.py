def leiaDin(msg):
    valid = False
    while not valid:
        din = str(input(msg)).replace(',', '.')
        if din.isalpha():
            print('ERRO! Digite um valor válido.')
        else:
            valid = True
            return float(din)
