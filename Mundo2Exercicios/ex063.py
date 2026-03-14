n = int(input('Digite um número inteiro: '))
cont = 1
anterior = 0
fibo = 1

print('Sequência de Fibonacci: ', end='')
print('{}'.format(anterior), end=' ')

while cont < n:
    print(fibo, end=' ')
    fibo += anterior
    cont += 1
    anterior = fibo - anterior