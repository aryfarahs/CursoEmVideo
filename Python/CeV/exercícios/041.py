from datetime import date

a = int(input('Em que ano você naceu? '))
b = date.today().year
c = b - a

if c <= 9:
    print(f'Com {c} anos, você é considerado \033[1;31mMIRIM.')

elif 9 < c <= 14:
    print(f'Com {c} anos, você é considerado \033[1;33mINFANTIL.')

elif 14 < c <= 19:
    print(f'Com {c} anos, você é considerado \033[1;32mJOVEM.')

elif 19 < c <= 25:
    print(f'Com {c} anos, você é considerado \033[1;34mSÊNIOR.')

else:
    print(f'Com {c} anos, você é considerado \033[1;35mMASTER.')