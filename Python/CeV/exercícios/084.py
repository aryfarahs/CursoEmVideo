dados = list()
pessoas = list()
tot = numero = 0
while True:
    dados.append(str(input('Nome: ')))
    dados. append(float(input(f'{"Peso: "}')))
    c = str(input('Deseja coninuar? [S/N] ')).upper()
    pessoas.append(dados[:])
    dados.clear()
    if c == 'N':
        break

print(f'Os dados foram: {pessoas}.')
print(f'Você cadastrou {len(pessoas)} pessoas.')
