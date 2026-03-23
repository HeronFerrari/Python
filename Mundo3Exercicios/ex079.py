lista = list()
while True:
    numero = int(input('Digite qualquer número inteiro (Digite 0 para encerrar): '))
           
    if numero == 0:
        break
    if lista.count(numero) >= 1: #Ou if numero in lista
        print('Esse número ja foi adicionado !')
    else:
        lista.append(numero)

print(f'Valores adicionados na lista: {sorted(lista)}')
print('Programa finalizado')