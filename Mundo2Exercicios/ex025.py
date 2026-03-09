numero = int(input('Digite um número: '))
antecessor = numero - 1
fatorial = numero

print('Calculando {}! '.format(numero))

while antecessor > 0:
    fatorial = fatorial * antecessor
    print('{}'.format(antecessor + 1), end=' ')
    print(' x ' if antecessor > 1 else ' x  {} ='.format(antecessor), end=' ')
    antecessor -= 1

'''Utilizando o laço for
numero = int(input('Digite um número: '))
fatorial = numero

for c in range(numero-1, 0, -1):
    fatorial = fatorial * c
'''

if numero == 0:
    fatorial = 1

print('{}'.format(fatorial))
#Dica: Biblioteca math possui função para calcular fatorial chamada factorial.