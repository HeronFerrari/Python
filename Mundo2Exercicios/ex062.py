termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
resposta = 10
total = 0

while resposta != 0: 
    total = total + resposta
    while cont < total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1

    print('PAUSA', end=' ')
    print('\nDigite 0 para encerrar', end=' ') 
    resposta = int(input('ou então digite quantos termos você deseja mostrar a mais: '))

print('FIM')
print('\nProgressão finalizada com {} termos mostrados.'.format(cont))