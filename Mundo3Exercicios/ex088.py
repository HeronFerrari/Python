from random import randint
from time import sleep
print(f'{' MEGA SENA ':=^50}')
jogadas = list()
palpites = list()

jogos = int(input('Quantos jogos você quer jogar ? '))

print()
print(f'{' || SORTEANDO NÚMEROS || ':=^50}')

for i in range(0,jogos):
    for j in range(0,6):
        jogadas.append(randint(0,60))
    palpites.append(jogadas)
    print(f'Jogo {i+1}: {sorted(palpites[i])}')
    sleep(1)
    jogadas.clear()

print('-=' * 5, f'{'Boa Sorte !':^10}', '-=' * 5)