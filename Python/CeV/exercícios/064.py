n = 0
s = 0
c = 0

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    s += 1
    c += n
print(f'Você digitou {s - 1} números. A soma entre eles é {c - 999}')
