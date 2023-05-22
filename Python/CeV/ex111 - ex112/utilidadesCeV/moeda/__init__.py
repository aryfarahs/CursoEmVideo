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
    return f'{"—" * 30}\n'\
           f'{"ANALISANDO VALORES":^30}\n'\
           f'{"—" * 30}\n'\
           f'Valor: \t\t\t\t{moeda(num)}\n'\
           f'Dobro: \t\t\t\t{dobro(num)}\n'\
           f'Metade: \t\t\t{metade(num)}\n'\
           f'Aumentar {moeda(taxup).replace("R$","")}%: \t{aumentar(num, taxup)}\n'\
           f'Diminuir {moeda(taxup).replace("R$","")}%: \t{diminuir(num, taxdn)}'