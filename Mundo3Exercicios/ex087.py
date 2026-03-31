numeros = list()
dados = list()
soma = terceira = maior = 0

for i in range(0,3):
    for j in range(0,3):
       numero = int(input(f'Digite o [{i}][{j}] número '))
       dados.append(numero)
    numeros.append(dados[:])
    dados.clear()

for i in range(0,3):
        print()
        for j in range(0,3):
            print(f'[{numeros[i][j]:^5}]',end='')

for i in range(0,3):
     for j in range(0,3):
        if numeros[i][j] % 2 == 0:
            soma += numeros[i][j]
        if j == 2:
            terceira += numeros[i][j] 
        if i == 1:
            if numeros[i][j] > maior:
                maior = numeros[i][j]

print()  
print(f'Soma dos valores pares: {soma}')
print(f'Soma dos valores da terceira coluna: {terceira}')
print(f'Maior valor da segunda linha: {maior}')