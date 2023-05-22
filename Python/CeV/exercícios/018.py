import math

a = int(input('Valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('Sen: {:.2f}\nCos: {:.2f}\nTg: {:.2f}'.format(sen, cos, tg))
