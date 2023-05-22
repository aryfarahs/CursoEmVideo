from utilidadesCeV import moeda, dado

din = dado.leiaDin('R$')
taxup0 = input('Quantos % deseja aumentar? ').replace(',', '.')
taxdn0 = input('Quantos % deseja diminuir? ').replace(',', '.')
taxup = float(taxup0)
taxdn = float(taxdn0)
print(moeda.resumo(din, taxup, taxdn))