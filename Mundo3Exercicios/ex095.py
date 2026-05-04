jogador = {}
gols = []
jogadores = list()

while True:
    jogador.clear()
    jogador['Nome'] = input(str('Digite o nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
    gols.clear()
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {c+1} ? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())

    resp = input('Quer continuar ? [S/N]').upper()[0]
    while resp not in 'SN':
        resp = input('ERRO ! Responda apenas S ou N: ').upper()[0]
    if resp == 'N':
        break

print('-='*30)
print(f'{'cod':<5}',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*60)
    
for k, v in enumerate(jogadores):
    print(f'{k:<5}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
    
print('-'*60)

while True:
    escolha = int(input('Quer ver os detalhes de qual jogador ? (999 para sair) '))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print(f'ERRO ! Não existe jogador com código {escolha}, tente novamente.')
    else:
        print('-'*60)
        print(f'Levantamento do jogador {jogadores[escolha]["Nome"]}: ')
        for i, g in enumerate(jogadores[escolha]['Gols']):
            print(f'- No jogo {i+1} fez {g} gols.')
        print('-'*60)

print('-='*30)
print('Finalizado ! Volte sempre !')
