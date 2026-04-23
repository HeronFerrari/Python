dict = {}
gols = []
jogadores = list()
totgols = 0

while True:
    nome = input(str('Digite o nome do jogador: ')).capitalize()
    dict['Nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou ? '))

    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {c+1} ? ')))
        totgols += gols[c]
    dict['Gols'] = gols[:]
    dict['Total'] = totgols
    jogadores.append(dict.copy())
    dict.clear()
    gols.clear()
    totgols = 0
    
    resp = input('Quer continuar ? [S/N]').upper()[0]
    if resp in 'N':
        break

print('-='*30)
print(f'{'cod':<5} {'nome':<10} {'gols':<10} {'total':>5}')
print('-'*60)
    
for k, v in enumerate(jogadores):
    print(f'{k:<5} {v["Nome"]:<10} {v["Gols"]} {v["Total"]:>5}')
    
print('-'*60)

print('Quer ver os detalhes de qual jogador ? ')
while True:
    escolha = int(input('Digite o código do jogador ou 999 para sair: '))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print(f'ERRO ! Não existe jogador com código {escolha}, tente novamente.')
        escolha = int(input('Digite o código do jogador ou 999 para sair: '))
    else:
        print('-'*60)
        print(f'Levantamento do jogador {jogadores[escolha]["Nome"]}: ')
        for i, g in enumerate(jogadores[escolha]['Gols']):
            print(f'- No jogo {i+1} fez {g} gols.')
        print('-'*60)

print('-='*30)
print('Finalizado ! Volte sempre !')
