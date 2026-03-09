#Variáveis com formatação de tipo inteiro, caso contrário seriam do tipo string
numero1 = int(input('\033[4mDigite o primeiro número: \033[m'))
numero2 = int(input('\033[4mDigite o segundo número: \033[m'))

#Versão mais verbosa
#print (' A soma entre', numero1, 'e', numero2, 'é igual a', numero1 + numero2 )

#Versão eficiente:
print('\033[1;34;45m A soma entre \033[1;32;42m{} e {}\033[m\033[1;34;45mé igual a \033[m\033[1;33;42m{}\033[m'.format(numero1, numero2, numero1 + numero2))