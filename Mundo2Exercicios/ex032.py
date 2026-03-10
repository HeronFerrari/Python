n = int(input('Digite um número inteiro para ver sua tabuada: '))
cont = 1

while n >= 0:
    while cont <= 10:
        print(f' {n} x {cont:^2} = {n * cont}')
        cont += 1
    cont = 1
    n = int(input('Digite um número inteiro para ver sua tabuada: '))

print('Programa encerrado.')
