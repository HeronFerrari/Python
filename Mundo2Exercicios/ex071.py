saque = int(input('Digite o valor a ser sacado: R$'))
total = saque
cedula = 50
totced = 0

print('-='*20)
print('BANCO CENTRAL DO PASSARINI')
print('-='*20)

while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
                print(f'Total de {totced} cédula(s) de R$ {cedula},00')
        totced = 0
        if cedula == 50:
                cedula = 20
        elif cedula == 20:
                cedula = 10
        elif cedula == 10:
              cedula = 1
        if total == 0:
                break

print('=-'*30)
print('\nOPERAÇÃO FINALIZADA.')
