frase = str(input('Digite uma frase para saber se ela é um palíndromo: ')).strip().upper()
frase = frase.replace(' ','')
tamanho = len(frase)

print('Tamanho: {} letras'.format(tamanho))

if tamanho % 2 == 0:
    print('Frase com número par de letras')
    parte1 = frase[0:tamanho//2]
    parte2 = frase[tamanho:tamanho//2-1:-1]
    print('Começo: {}'.format(parte1))
    print('Final ao contrário: {}'.format(parte2))
    for c in range(0,tamanho//2):
        if parte1[c] == parte2[c]:
            print('Parte 1 letra \033[32m{}\033[m é igual parte 2 letra {}'.format(parte1[c], parte2[c]))
        else:
            print('Parte 1 letra \033[31m{}\033[m é diferente de parte 2 letra {}'.format(parte1[c], parte2[c]))
    print('Frase completa: {}'.format(parte1+parte2[::-1]))
else:
    print('Frase com número ímpar de letras')
    parte1 = frase[0:tamanho//2]
    parte2 = frase[tamanho:tamanho//2:-1]
    print('Começo: {}'.format(parte1))
    print('Final ao contrário: {}'.format(parte2))
    for c in range(0,tamanho//2):
        if parte1[c] == parte2[c]:
            print('Parte 1 letra \033[32m{}\033[m é igual parte 2 letra {}'.format(parte1[c], parte2[c]))
        else:
            print('Parte 1 letra \033[31m{}\033[m é diferente de parte 2 letra {}'.format(parte1[c], parte2[c]))
    print('Letra do meio: {}'.format(frase[tamanho//2]))
    print(parte1+frase[tamanho//2]+parte2[::-1])

if parte1 == parte2:
    print('A frase é um \033[32mpalíndromo\033[m')
else:
    print('A frase \033[31mnão é\033[m um palíndromo')

#FORMA BEM MAIS SIMPLES

'''
frase = str(input('Digite uma frase para saber se ela é um palíndromo: ')).strip().upper()
palavras = frase.spli()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase é um \033[32mpalíndromo\033[m')
else:
    print('A frase \033[31mnão é\033[m um palíndromo')

Outra opção é trocar a linha inverso = '' e também o laço for inteiro por: inverso = junto[::-1].
'''