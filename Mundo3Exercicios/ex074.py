from random import randint
tupla = (randint(0,99), randint(0,99), randint(0,99), randint(0,99), randint(0,99))

print(f"Valores sorteados: {tupla}")

''' 
#Versão mais verbosa
for c in range(0,5):
    if c == 0:
        maior = menor = tupla[c]
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
'''
#Versão simples com método min e max.
print(f'O maior número é {max(tupla)} e o menor é {min(tupla)}')
    