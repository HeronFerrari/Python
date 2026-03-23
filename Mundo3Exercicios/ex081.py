lista = list()
while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    resposta = input('Deseja continuar ? [S/N]').strip().upper()[0]
    if resposta != 'S':
        break


print(f'Números digitados: {len(lista)}')
print(f'Lista ordenada de forma decrescente: {sorted(lista, reverse=True)}')
if lista.count(5) >= 1:
    print(f'O valor 5 está na lista, na posição {lista.index(5)}')
else:
    print('O valor 5 não está na lista !')