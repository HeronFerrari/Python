from random import randint
from time import sleep
j1 = randint(1,6)
j2 = randint(1,6)
j3 = randint(1,6)
j4 = randint(1,6)
resultados = {'Jogador 1': j1, 'Jogador 2': j2, 'Jogador 3': j3, 'Jogador 4': j4}

for k, v in resultados.items():
    print(f'Jogador {k} tirou: {v}')
    sleep(1)
sleep(1)
print('-=' * 20)
sleep(1)
print('Ranking dos jogadores:')
sleep(1)

rank = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

for i, (k, v) in enumerate(rank):
    print(f'  {i+1}º lugar: {k} com {v}')