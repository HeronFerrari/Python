def leiaDinheiro(msg):
    while True:
        print(msg, end='')
        valor = input().replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;30;31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            return float(valor)