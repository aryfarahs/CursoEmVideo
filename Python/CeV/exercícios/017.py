import math
c1=float(input('Digite o primeiro cateto: '))
c2=float(input('Agora o segundo: '))
h = math.pow(c1 , 2) + math.pow(c2 , 2)
print('A hipotenusa do triangulo de lados {} e {} mede {}'.format(c1 , c2 , math.sqrt(h)))