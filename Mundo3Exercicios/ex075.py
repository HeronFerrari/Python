tupla =(int(input('Digite o valor: ')),
        int(input('Digite o valor: ')),
        int(input('Digite o valor: ')),
        int(input('Digite o valor: ')))

cont = pos = 0

for c in range(0,4):
    if tupla[c] == 9:
        cont += 1

print(f'Valor 9 apareceu {cont} vezes')
#Ou print(f'Valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 aparece na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não existe na tupla')

print(f'Os valores pares digitados foram: ',end='')

for c in range(0,len(tupla)):
     if tupla[c] % 2 == 0:
        print(tupla[c],end=' ')

#Versão verbosa sem função index para parte de achar o numero 3.

'''for c in range(0, len(tupla)):
    if tupla[c] == 3:
        pos = c+1
        break

if pos <= 0:
    print('Não há número 3 na lista')
else:
    print(f'Valor 3 apareceu na posição {pos}')
'''