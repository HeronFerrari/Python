numero = int(input('Digite um numero inteiro: '))
base = int(input('Selecione a base de conversão digitando o número correspondente: \nBinário: 1\nOctal: 2\nHexadecimal: 3\nNúmero da base selecionada: '))
if base == 1:
    print('O número {} convertido para binário é: {}'.format(numero,bin(numero)[2:]))
elif base == 2:
    print ('O número {} convertido para octal é: {}'.format(numero,oct(numero)[2:]))
elif base == 3:
    print('O número {} convertido para hexadecimal é: {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida. Por favor, selecione uma base de conversão válida (1 , 2 ou 3).')
    