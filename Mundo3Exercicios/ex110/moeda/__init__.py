def aumentar(num = 0, taxa = 0, boolean=False):
    if boolean:
        return moeda(num + (num * taxa / 100))
    else:
        return num + (num * taxa / 100)

def diminuir(num = 0, taxa = 0, boolean=False):
    if boolean:
        return moeda(num - (num * taxa / 100))
    else:
        return num - (num * taxa / 100)

def dobro(num = 0,boolean=False):
    if boolean:
        return moeda(num * 2)
    else:
        return num * 2

def metade(num = 0, boolean=False):
    if boolean:
        return moeda(num / 2)
    else:
        return num / 2

def moeda(num = 0, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.', ',')

def resumo(num = 0, acrescimo = 10, decrescimo = 5):
    print('-'*70)
    print(f'{f'RESUMO DE {moeda(num)}'.center(70)}')
    print('-'*70)
    print(f'{f'A metade de {moeda(num)} é'.ljust(40)}{(metade(num, True)).rjust(30)}')
    print(f'{f'O dobro de {moeda(num)} é'.ljust(40)}{(dobro(num, True)).rjust(30)}')
    print(f'{f'A quantia {moeda(num)} aumentada em {acrescimo}% é'.ljust(40)}{aumentar(num, acrescimo, True).rjust(30)}')
    print(f'{f'A quantia {moeda(num)} diminuida em {decrescimo}% é'.ljust(40)}{diminuir(num, decrescimo, True).rjust(30)}')
    print('-' * 70)
