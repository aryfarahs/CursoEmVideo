def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =',end=' ')
        f *= c
    return f

num = int(input('Deseja ver o fatorial de qual número? '))
bool = str(input('Deseja ver a sequencia de conta? [S/N] ')).upper()
if bool in 'S':
    bool = True
else:
    bool = False
print(fatorial(num, bool))