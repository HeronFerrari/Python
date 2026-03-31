listona = list()

while True:
    nome = str(input('Nome:'))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    listona.append([nome,[n1,n2],media]) #Criando uma lista e adicionando uma lista que contem um [valor, uma [lista com dois valores], e mais outro valot]. 

    resposta = str(input('Quer continuar ? [S/N]')).strip().upper()
    if resposta != 'S':
        break

print('-'*30)
print(f'{"No.":>4} {"NOME":<10}{'MEDIA':>12}')
print('-'*30)
 
for i in range(0,len(listona)):
    print(f'{i:<4}{listona[i][0]:<10}',end='')
    for j in range(0,1):
        print(f'{listona[i][2]:>12.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno (999 para interromper) ? '))
    if opc == 999:
        break
    if opc < len(listona):
        print(f'Notas de {listona[opc][0]}: {listona[opc][1]}')


print('FINALIZANDO...')
print('--- VOLTE SEMPRE ! ---')