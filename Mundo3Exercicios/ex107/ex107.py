import moeda

numero = float(input('Digite um valor R$: '))

print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'A metade de {numero} é {moeda.metade(numero)}')
print(f'Aumentando 28% de {numero} temos {moeda.aumentar(numero, 28):.2f}')
print(f'Diminuindo 17% de {numero} temos {moeda.diminuir(numero, 17):.2f}')

