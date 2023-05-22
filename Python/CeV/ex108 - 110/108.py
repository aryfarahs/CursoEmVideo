import moeda

din = int(input('R$'))
taxup = int(input('Quantos % deseja aumentar? '))
taxdn = int(input('Quantos % deseja diminuir? '))
print(moeda.resumo(din, taxup, taxdn))