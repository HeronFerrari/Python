def leiaDinheiro(msg):
    valido = False
    while not valido:
        n = str(input(msg)).replace(',', '.')
        if n.isalpha() or n.strip() == '':
            print('\033[31mERRO, digite um número válido\033[m ')
        else:
            valido = True
            return float(n)