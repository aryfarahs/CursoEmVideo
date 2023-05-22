v = float(input('Qual é a distância da viagem? '))
m = 0.50 * v
n = 0.45 * v
print(f'Você fará uma viagem de {v} km')
print(f'O valor da passagem será R${m:.2f}') if v <= 200 else print(f'O valor da passagem será R${n:.2f}')