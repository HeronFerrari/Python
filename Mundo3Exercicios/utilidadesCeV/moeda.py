def aumentar(num, taxa, boolean=False):
    if boolean:
        return moeda(num + (num * taxa / 100))
    else:
        return num + (num * taxa / 100)

def diminuir(num, taxa, boolean=False):
    if boolean:
        return moeda(num - (num * taxa / 100))
    else:
        return num - (num * taxa / 100)

def dobro(num,boolean=False):
    if boolean:
        return moeda(num * 2)
    else:
        return num * 2

def metade(num, boolean=False):
    if boolean:
        return moeda(num / 2)
    else:
        return num / 2

def moeda(num, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.', ',')

def resumo(num=0, aum=10, dim=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'{'Preço analisado:':<20}{moeda(num):>20}')
    print(f'{'Dobro de preço:':<20}{dobro(num, True):>20}')
    print(f'{'Metade do preço:':<20}{metade(num, True):>20}')
    print(f"{f'Com aumento de {aum}%:':<20}{aumentar(num, aum, True):>20}")
    print(f"{f'Com redução de {dim}%:':<20}{diminuir(num, dim, True):>20}")
    print('-' * 40)