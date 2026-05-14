import moeda

numero = float(input('Digite um valor R$ '))

print(f'O dobro de {moeda.moeda(numero)} é {(moeda.dobro(numero,True))}')
print(f'A metade de {moeda.moeda(numero)} é {(moeda.metade(numero,False))}')
print(f'Aumentando 28% de {moeda.moeda(numero)} temos {(moeda.aumentar(numero, 28,True))}')
print(f'Diminuindo 17% de {moeda.moeda(numero)} temos {(moeda.diminuir(numero, 17))}')

