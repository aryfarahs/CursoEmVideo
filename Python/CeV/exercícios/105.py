def notas(*num, sit=False):
    """
    -> Função para notas da sala:
    :param num: notas dos alunos (1 ou mais)
    :param sit: situação da média da classe, valor opcional
    :return: dicionário com informações da situação da turma
    """
    d = {}
    d['total'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['med'] = sum(num) / len(num)
    if sit:
        if d['med'] >= 7:
            d['sit'] = 'BOA'
        elif d['med'] < 7:
            d['sit'] = 'RAZOAVEL'
        elif ['med'] < 5:
            d['sit'] = 'RUIM'
    print(d)

notas(5, 7, 8, 10, sit=True)
notas(7.5, 8.9, 4.0, 6.8, sit=True)
help(notas)
