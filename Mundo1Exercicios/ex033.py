numeros = str(input('Digite \033[34mtrês números inteiros\033[m separados por espaços: '))
numeros = numeros.split()
n1 = int(numeros[0])
n2 = int(numeros[1])
n3 = int(numeros[2])
#Verificando menor e maior número
menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando o maior número
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O \033[31mmenor\033[m número é: {}'.format(menor))
print('O \033[32mmaior\033[m número é: {}'.format(maior))
