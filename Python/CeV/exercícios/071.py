print('-'*30)
print('{:^30}'.format('BANCO FARAHS'))
print('-'*30)
q = int(input('Quanto deseja sacar? [R$] ' ))
tot = q
ced = 50
tc = 0

while True:
    if tot >= ced:
        tot -= ced
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tc = 0
        if tot == 0:
            break
print('Volte sempre!')