r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    print('Com essas retas, é possivel formar um triângulo juntando suas extremidades.')

else:
    print('Ao juntarmos as extremidades dessas retas, NÃO será possível formar um triângulo.')