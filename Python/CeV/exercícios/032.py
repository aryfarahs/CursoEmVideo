a = int(input('Qual ano quer analizar? (Use 0 como o presente): '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano de {a} é BISSEXTO.')
else:
    print(f'O ano de {a} NÃO é BISSEXTO.')