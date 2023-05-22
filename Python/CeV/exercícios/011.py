l=float(input('Largura da parede(m): '))
h=float(input('Altura da parede(m): '))
p=int(input('Número de paredes: '))
print('O prédio tem {} paredes com {:.2f}m². Você precisará de {:.0f}L de tinta.'.format(p,h*l,((h*l)/2)*p))