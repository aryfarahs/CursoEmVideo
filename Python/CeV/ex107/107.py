import moeda

din = int(input('R$'))
taxup = int(input('Quantos % deseja aumentar? '))
taxdn = int(input('Quantos % deseja diminuir? '))
print(f'Valor: R${din:.2f}\n'
      f'Dobro: R${moeda.dobro(din):.2f}\n'
      f'Metade: R${moeda.metade(din):.2f}\n'
      f'Aumentar {taxup}%: R${moeda.aumentar(din, taxup):.2f}\n'
      f'Diminuir {taxdn}%: R${moeda.diminuir(din,taxdn):.2f}')
