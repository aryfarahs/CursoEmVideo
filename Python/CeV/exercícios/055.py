maior = 0
menor = 0

for p in range(1 , 6):
    kg = float(input(f'Peso da {p}ª pessoa (Kg): '))
    if p == 1:
        maior = kg
        menor = kg
    else:
        if maior < kg:
            maior = kg
        if menor > kg:
            menor = kg

print(f'O maior peso lido foi de {maior:.1f} Kg.')
print(f'O menor peso lido foi de {menor:.1f} Kg.')

