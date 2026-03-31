numeros = [[],[]]

for c in range(0,7):
    numero = int(input(f'Digite o {c+1}º valor: '))
    while numero in numeros[0] or numero in numeros[1]:
        numero = int(input(f'Valor já está cadastrado ! Digite o {c+1}º valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f'Números pares: {sorted(numeros[0])}')
print(f'Números ímpares: {sorted(numeros[1])}')     