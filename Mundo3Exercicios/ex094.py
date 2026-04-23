pessoa = dict()
pessoas = list()
mulheres = list()
idadeacima = list()
totidade = 0

while True:
    pessoa['Nome'] = str(input('Digite seu nome: ')).capitalize()
    pessoa['Sexo'] = str(input('Digite o seu sexo: ')).upper()[0]
    pessoa['Idade'] = int(input('Digite a sua idade: '))
    pessoas.append(pessoa.copy())
    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break

for c in pessoas:
    totidade += c['Idade']
    if c['Sexo'] == 'F':
        mulheres.append(c.copy())

for c in pessoas:
    if c['Idade'] > totidade/len(pessoas):
        idadeacima.append(c.copy())

print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('-='*30)
print(f'A média de idade do grupo é de {totidade/len(pessoas):.2f} anos.')
print('-='*30)
print(f'As mulheres cadastradas foram: ')
for c in mulheres:
    print(f'{c["Nome"]}')

print('-='*30)
print(f'As pessoas com idade acima da média são: ')
for c in idadeacima:
    print(f'Nome: {c["Nome"]}; Sexo: {c["Sexo"]}; Idade: {c["Idade"]}.')

print('Programa Encerrado')