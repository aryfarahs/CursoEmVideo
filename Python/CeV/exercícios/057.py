s = str(input('Qual é seu sexo? ')).strip().upper()[0]
while s not in 'MmFf':
    print('\033[1;30;41mERRO! Tente novamente.\033[m')
    s = str(input('Qual é seu sexo? ')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')
