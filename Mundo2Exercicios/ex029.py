n = cont = soma = 0
print('Contador de números inteiros,', end=' ')
print('digite 999 para parar o programa.')
n = int(input('Digite um número inteiro:'))

while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro: '))  

print('Programa finalizado. {} números foram digitados.'.format(cont - 1))
print('A soma dos {} números digitados é {}.'.format(cont, soma))