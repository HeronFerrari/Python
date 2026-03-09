resposta = 'S'
soma = cont = maior = menor = 0

while resposta != 'N':
    num = int(input('Digite um número: '))
    soma += num
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    resposta = input('Deseja continuar? [S/N] ').upper().strip()

print('A média dos {} números digitados é {:.2f}.'.format(cont, soma / cont ))
print('O maior número digitado foi {}, e o menor número foi {}.'.format(maior, menor))