from random import randint

def sorteia(lista): 
    for c in range(0,5):
        lista.append(randint(1,100))
    print(f'Os números sorteados foram: {lista}')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos números pares é: {soma}')



numeros = []
sorteia(numeros)
somaPar(numeros)
