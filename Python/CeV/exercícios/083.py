m = str(input('Digite uma expressão: '))
p = []
for simb in m:
    if simb == '(':
        p.append('(')
    elif simb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Sua expressão está \033[1;32mválida!\033[m')
else:
    print('Sua expressão está \033[1;31minválida\033[m!')
