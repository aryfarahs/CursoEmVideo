def area(l, c):
    m = l * c
    print(f'A área de um terreno com medidas {l:.2f}x{c:.2f}é de {m:.2f} metros quadrados')

#Programa principal:
print('Controle de terrenos')
print('--------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)


