from time import sleep; from random import choice
print('Vamos jogar JOKENPÔ ?')
sleep(0.5)
escolha = input('Escolha sua jogada !\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n ')
if escolha == '1':
    escolha = 'Pedra'
elif escolha == '2':
    escolha = 'Papel'
elif escolha == '3':
    escolha = 'Tesoura'
else:
    print('Opção inválida. Por favor, escolha entre 1, 2 ou 3.')
    exit()
sleep(1.0)
print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('PÔ !')
sleep(0.5)
computador = choice(['Pedra', 'Papel', 'Tesoura'])
print('Computador: {}\nVocê: {}'.format(computador, escolha))
if computador == escolha:
    print('\033[33mEmpate !\033[m')
elif (computador == 'Pedra' and escolha == 'Tesoura') or (computador == 'Papel' and escolha == 'Pedra') or (computador == 'Tesoura' and escolha == 'Papel'):
    print('\033[34mO computador venceu !\033[m')
else:
    print('\033[32mVocê venceu !\033[m')