termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao

if razao > 0:
    print('Os 10 primeiros termos da PA crescente são: ')
elif razao < 0:
    print('Os 10 primeiros termos da PA decrescente são: ')

for c in range(termo, decimo + razao, razao): #decimo + razao para incluir o decimo termo
    print('{}'.format(c), end='-')

print('Fim')
