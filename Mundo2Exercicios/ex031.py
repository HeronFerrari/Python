n = cont = soma = 0
print('Digite um valor (999 para parar): ')
while n != 999:
    cont += 1
    soma += n
    if n == 999:
        break
    n = int(input('Digite um número inteiro: '))
print(f'Soma dos números é {soma}')