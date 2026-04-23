nome = input(str('Digite o nome do jogador: ')).capitalize()
dict = {}
dict['Nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou ? '))
gols = []

for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols ele fez na partida {c+1} ? ')))
dict['Gols'] = gols[:]
dict['Total'] = sum(gols)

print('-='*30)

print(dict)

print('-='*30)

for k, v in dict.items():
    print(f'O campo {k} tem valor {v}')

print('-='*30)

print(f'O jogador {dict["Nome"]} jogou {partidas} partidas.')

for k, v in enumerate(dict['Gols']):
    print(f'  => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {dict["Total"]} gols.')