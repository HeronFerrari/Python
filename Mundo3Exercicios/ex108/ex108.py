import moeda

numero = float(input('Digite um valor R$ '))

print(f'O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}')
print(f'A metade de {moeda.moeda(numero)} é {moeda.moeda(moeda.metade(numero))}')
print(f'Aumentando 28% de {moeda.moeda(numero)} temos {moeda.moeda(moeda.aumentar(numero, 28))}')
print(f'Diminuindo 17% de {moeda.moeda(numero)} temos {moeda.moeda(moeda.diminuir(numero, 17))}')

