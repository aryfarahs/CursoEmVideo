def aumentar(prc=0, tax=0, formatar=True):
    res = prc + (prc * tax/100)
    return res if formatar is False else moeda(res)


def diminuir(prc=0, tax=0, formatar=True):
    res = prc - (prc * tax / 100)
    return res if formatar is False else moeda(res)


def metade(prc=0, formatar=True):
    res = prc / 2
    return res if formatar is False else moeda(res)


def dobro(prc=0, formatar=True):
    res = prc * 2
    return res if formatar is False else moeda(res)


def moeda(prc=0, typ='R$'):
    return f'{typ}{prc:>.2f}'.replace('.', ',')


def resumo(num=0, taxup=10, taxdn=10):
    return f'{"—" * 40}\n'\
           f'{"ANALISANDO VALORES":^40}\n'\
           f'{"—" * 40}\n'\
           f'Valor: {moeda(num)}\n'\
           f'Dobro: {dobro(num)}\n'\
           f'Metade: {metade(num)}\n'\
           f'Aumentar {taxup}%: {aumentar(num, taxup)}\n'\
           f'Diminuir {taxup}%: {diminuir(num, taxdn)}'