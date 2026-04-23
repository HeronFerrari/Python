dict = {}
jogadores = []
gols = []

while True:
    dict["Nome"] = input(str('Digite o nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {dict["Nome"]} jogou ? '))

    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {c+1} ? ')))

    dict['Gols'] = gols[:]
    dict['Total'] = sum(dict['Gols'])
    jogadores.append(dict.copy())
    dict.clear()
    gols.clear()
    
    resp = input('Quer continuar ? [S/N]').upper()[0]
    
    if resp in 'N':
        break

for i, v in enumerate(jogadores):
    print(f'{i} {v["Nome"]} {v["Gols"]} {v["Total"]}')