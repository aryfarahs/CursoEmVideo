from time import sleep

for cont in range(10 , 0 , -1):
    print(cont)
    sleep(0.8)

print('\033[1;4;41;30m{: ^30}\033[m'.format('BOOM!'))
