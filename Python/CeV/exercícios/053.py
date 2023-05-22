f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''

for l in range(len(j) - 1 , -1 , -1):
    i += j[l]

print(j)
print(i)

if j == i:
    print('Essa frase \033[1;32mé\033[m um \033[1;36mPALÍNDROMO!')
else:
    print('A frase \033[1;31mnão\033[m é um \033[1;36mPALÍNDROMO.')