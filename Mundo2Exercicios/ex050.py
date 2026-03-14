
s = 0
cont = 0
for c in range (0,6):
    n = int(input('Digite o {}º número inteiro: '.format(c+1)))
    if n % 2 == 0:
        s = s + n
        cont += 1

print('A soma dos {} números pares é: {}'.format(cont,s))