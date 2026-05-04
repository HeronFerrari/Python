def fatorial(num, show=False):
    """Calcula o fatorial de um número.
    :param num: O número para calcular o fatorial.
    :param show: Se True, mostra o processo de cálculo."""
    
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    if show:
        for i in range(num, 0, -1):
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return fat

print(fatorial(5, show=True))
print(fatorial(8, show=False))