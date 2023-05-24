times = ('América-MG', 'Athletico-PR','Atlético-MG','Bahia','Botafogo','Corinthians','Coritiba',
         'Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Bragantino','Santos','São Paulo','Vasco da Gama')

print('5 primeiros times: ', end='')
for c in range(5):
    print(times[c], end=', ')
print()

print('4 piores: ', end='')
for c in range(len(times)-1, 15, -1):
    print(times[c], end=', ')
print()

print(sorted(times))
i = times.index('Coritiba')
print(f'Coritiba está na posição {i}')