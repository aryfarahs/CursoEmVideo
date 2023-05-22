p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('E a sua altura? (m) '))
imc = p / a**2

print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está \033[1;36mabaixo do peso.\033[m Se alimente melhor! (18.5-)')

elif 18.5 <= imc <= 24.9:
    print('Seu IMC é \033[1;32mnormal.\033[m (18.6 - 24.9)')

elif 25 <= imc <= 29.9:
    print('Você está com \033[1;33msobrepeso, se cuide!\033[m (25.0 - 29.9)')

elif 30 <= imc <= 39.9:
    print('Cuidado! Você está com \033[1;31mobesidade.\033[m (30.0 - 39.9)')

else:
    print('Você está com \033[1;30;41mobesidade severa!\033[m Procure ajuda urgentemente! (40.0+)')