numeros = list()
dados = list()

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