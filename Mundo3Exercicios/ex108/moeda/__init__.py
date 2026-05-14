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

def moeda(num, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.', ',')