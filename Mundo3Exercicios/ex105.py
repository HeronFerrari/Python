def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic = {}
    dic['Notas'] = len(notas)
    for i, v in enumerate(notas):
        if i == 0:
            dic['Maior'] = v
            dic['Menor'] = v
        if v > dic['Maior']:
            dic['Maior'] = v
        if v < dic['Menor']:
            dic['Menor'] = v
    dic['Media'] = sum(notas) / len(notas)
    if sit == True:
        if dic['Media'] >= 6:
            dic['Situação'] = 'Aprovado'
        elif dic['Media'] >= 4 and dic['Media'] < 6:
            dic['Situação'] = 'Recuperação'
        else:
            dic['Situação'] = 'Reprovado'
    return dic

resp = notas(5.5,2.1,2.3,9.3,8.9, sit=True)
resp2 = notas(5.5,5.1,8,9,8,3,1,10,2,3)
print(resp)
print(resp2)

#Dica: Pode ser usado min, max, sum e len pra facilitar.