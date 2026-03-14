termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0

while cont < 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('FIM')