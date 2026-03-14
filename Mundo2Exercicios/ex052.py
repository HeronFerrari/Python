numero = int(input('Digite um número inteiro: '))
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

div = primos[0]
quo = numero // div

if numero == 2:
        print('O 2 é o único número par e também primo !')

for c in range (0,numero):

    div = primos[c]
    print('Dividindo {} por {}'.format(numero, div))
    quo = numero // div
    resto = numero % div
    print('Quociente {} e resto: {}'.format(quo, resto))
    if quo > div and resto == 0:
        print('O número {} não é primo'.format(numero))
        break
    elif quo <= div and resto > 0:
        print('O número {} dividido por {} tem quociente ({}) menor que o divisor, e resto maior que zero, portanto é primo'.format(numero, div, quo))
        break
    
    #Dicas para saber se o número é primo (Divisível somente por 1 ou por ele mesmo):
        #Se a soma dos números forem múltiplos de 3 então o numero é divisível por 3.
        #Todo numero par é divisível por 2 com resto 0.
        #Todo número terminado em 0 e 5 é divisível por 5 com resto 0.

'''Versão bem mais simples:
numero = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1,numero+1):
    if numero % c == 0:
      tot += 1
      print('\033[33m' end='')
    else:
      print('\033[31m' end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')'''