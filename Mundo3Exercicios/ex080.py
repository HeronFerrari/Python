lista = list()
c = 0

while True:
    numero = int(input('Digite seu número '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f'Adicionado ao final da lista: {lista}')
        c += 1
    else:
        for i in range(0, len(lista)):
            # Compara o elemento atual com o próximo
                if numero <= lista[i]:
                    print(f'Inserindo {numero} na posição {i}')
                    lista.insert(i,numero)
                    print(f'Lista atual: {lista}')         
                    break
    resposta = input('Quer continuar ? [S/N]').strip().upper()[0]
    if resposta != 'S':
        break


print("-" * 20)
print(f'Lista final ordenada: {lista}')
