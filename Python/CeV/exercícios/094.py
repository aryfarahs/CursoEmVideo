dados = {}
pessoas = []
mulheres = []
soma = média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite somente "M" ou "F"')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    soma += dados['idade']
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite somente "S" ou "N"')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
média = soma / len(pessoas)
print(f'B) A média de idade é de {média:.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) lista das pessoas que estão com a idade acima da média: ')
for p in pessoas:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\033[1m<< ENCERRADO >>')