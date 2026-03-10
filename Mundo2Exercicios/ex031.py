n = cont = soma = 0
print('Digite um valor (999 para parar): ')
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Soma dos {cont} números é {soma}')