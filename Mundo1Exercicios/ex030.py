numero = int(input('\033[37mDigite um número inteiro:\033[m '))
if numero % 2 == 0:
    print('O número {} é \033[34mpar\033[m.'.format(numero))
else:
    print('O número {} é \033[32mímpar\033[m.'.format(numero))
    