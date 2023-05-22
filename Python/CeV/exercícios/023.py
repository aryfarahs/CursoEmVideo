frase = int(input('Digite um número:'))
u = frase // 1 % 10
d = frase // 10 % 10
c = frase // 100 % 10
m = frase // 1000 % 10
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhares: {m}')