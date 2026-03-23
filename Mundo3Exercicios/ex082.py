lista = list()
while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    resposta = input('Deseja continuar ? [S/N]').strip().upper()[0]
    if resposta != 'S':
        break

listapares = list()
listaimpares = list()

for i in range(0,len(lista)):
    if lista[i] % 2 == 0:
        listapares.append(lista[i])
    else:
        listaimpares.append(lista[i])

print(f'Lista completa {lista}')
print(f'Lista dos números pares {listapares}')
print(f'Lista dos números ímpares {listaimpares}')