saque = int(input('Digite o valor a ser sacado: R$'))
cedula50 = saque // 50
cedula20 = saque // 20
cedula10 = saque // 10
cedula1 = saque // 1

print('-='*20)
print('BANCO CENTRAL DO PASSARINI')
print('-='*20)

if saque - cedula50*50 > 0:
    saque = saque - cedula50*50
    cedula20 = saque // 20
if saque - cedula20 * 20 > 0:
        saque = saque - cedula20 * 20
        cedula10 = saque // 10
if saque - cedula10 * 10 > 0:
        saque = saque - cedula10 * 10
        cedula1 = saque // 1

print(f'Cédulas de R$ 50: {cedula50}\nCédulas de R$ 20: {cedula20}\nCédulas de R$ 10: {cedula10}\nCédulas de R$ 01: {cedula1}')
print('\nOPERAÇÃO FINALIZADA.')