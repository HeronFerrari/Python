produtos = ('Caderno', 20.99, 'Lápis', 3.5, 'Mochila', 99.99, 'Estojo', 23.5, 'Caneta', 2.0, 'Régua', 5.5, 'Corretivo', 10.99, 'Borracha', 4.5)

print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)

for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<40}R$',end='')
    else:
        print(f'{produtos[c]:>7.2f}')

print('-'*50)