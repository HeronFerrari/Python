numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print('O primeiro número {} é maior que o segundo número {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('O segundo número {} é maior que o primeiro número {}'.format(numero2, numero1))
else:
    print('Ambos os números são iguais.')
