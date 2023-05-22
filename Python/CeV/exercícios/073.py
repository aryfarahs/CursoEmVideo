t = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
     'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
     'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
print('LISTA DO BRASILEIRÂO 19/11/2022:')
print(f'\033[1;32mCinco primeiros\033[m colocados: {t[0:5]}')
print(f'\033[1;31mQuatro últimos\033[m colocados: {t[16:20]}')
print(f'Times em ordem \033[1;35malfabética\033[m: {sorted(t)}')
c = 'Coritiba'
print(f'O Coritiba se encontra na {t.index(c) + 1} posição')