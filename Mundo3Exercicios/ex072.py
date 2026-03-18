extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero < 0 or numero > 20:
        numero = int(input('Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o numero {extenso[numero]}')
        resposta = input('Deseja continuar ? [S/N]').upper()[0]
        if resposta != 'S':
            break

print('Programa finalizado')