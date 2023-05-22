print('{:=^40}'.format('LOJAS FARAH'))
p = float(input('Boa tarde. Qual é o valor da sua conta? (R$)'))

print('[ 1 ] à vista no DINHEIRO/CHEQUE; \n[ 2 ] à vista no cartão; \n[ 3 ] 2x no cartão; \n[ 4 ] 3x ou mais no cartão.')

e = int(input('Selicione uma forma de pagamento: '))

a = 10/100*p
b = 5/100*p
c = p
d = 20/100*p

if e == 1:
    print(f'À vista no dinehiro você tem 10% de desconto. Sua compra sairá por R${p - a:.2f}')

elif e == 2:
    print(f'À vista no cartão você tem 5% de desconto. Sua compra sairá por R${p - b:.2f}')

elif e == 3:
    print(f'Parcelando sua compra em 2x, o valor dela não é alterado. O preço é de R${c:.2f}')

elif e == 4:
    print(f'Ao parcelar sua conta em 3 ou mais vezes, um juros de 20% é aplicado à ela. O preço final é de R${p + d:.2f}')

else:
    print('\033[1;30;41mOPÇÂO INDISPONÍVEL. TENTE NOVAMENTE.\033[m')
