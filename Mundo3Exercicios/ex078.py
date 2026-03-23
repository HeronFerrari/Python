lista = list()
indicemaior = list()
indicemenor = list()

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

for cont, n in enumerate(lista):
    if cont == 0:
        maior = menor = lista[cont]
    if maior <= lista[cont]:
        maior = lista[cont]
    if menor >= lista[cont]:
        menor = lista[cont]

for pos, n in enumerate(lista):
    if n == maior:
        indicemaior.append(pos)
    elif n == menor:
        indicemenor.append(pos)


print(f'Lista digitada: {lista}')
print(f'Maior número: {maior}, nas posições: {indicemaior}')
print(f'Menor número: {menor}, nas posições: {indicemenor}')


#print(f'Maior da lista: Pos:{lista.index(max)}, Valor:{lista.max}')
#print(f'Maior da lista: Pos:{lista.index(min.lista)}, Valor:{min.lista}')
