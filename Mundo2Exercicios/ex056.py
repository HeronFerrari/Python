somaidade = 0
media = 0
maisvelho = 0
nomevelho = ''
mulheres = 0

for c in range(0,4):
    print('----- {}ª PESSOA ----- '.format(c+1))
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    somaidade += idade
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1

media = somaidade / 4
print('\nA média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho, nomevelho,))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))

'''
for c in range(0,4):
    print('----- {}ª PESSOA ----- '.format(c+1))
    print('Nome: {}\nIdade: {}\nSexo: {}'.format(nome, idade, sexo))
'''

#print('A média de idade do grupo é de {} anos'.format(media))