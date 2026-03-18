palavras = ('Arroz', 'Feijao', 'Maracuja','stf','Rapadura', 'Agua', 'Regrigerante', 'Pizza', 'Cafe', 'Banana')

vogais = 'AaEeIiOoUu'

for palavra in palavras:
    tem = False
    for letra in palavra:
        if letra in vogais:
            tem = True
            break
    if tem:
        print(f'Na palavra {palavra.upper()} \033[32mtemos\033[m as vogais (',end='')
        for letra in palavra:
            if letra in vogais:
                print(f'{letra}',end='-')
        print(')')
    else:
        print(f'\033[31mNão temos\033[m vogal na palavra {palavra.upper()}')