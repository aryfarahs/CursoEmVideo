def voto(ano):
    from datetime import date
    now = date.today().year
    old = now - ano
    if old < 16:
        print(f'Com {old} anos, o voto é PROIBIDO!')
    elif 16 <= old < 18 or old >= 65:
        print(f'Com {old} anos, o voto é OPCIONAL!')
    elif 65 > old >= 18:
        print(f'Com {old} anos, o voto é OBRIGATÓRIO')

year = int(input('Em que ano você nasceu? '))
voto(year)