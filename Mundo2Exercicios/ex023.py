from random import randint; from time import sleep
computador = randint(0,10)
print('Olá, vamos jogar um jogo de adivinhação ?')
sleep(1)
print('Estou pensando em um número entre 0 e 10, tente adivinhar qual é ele')
sleep(1)

palpite = int(input('Digite seu palpite: '))
tentativas = 1
while palpite != computador:
    tentativas += 1
    if palpite < computador:
        print('O número é maior do que {} !'.format(palpite))
    else:
        print('O número é menor do que {} !'.format(palpite))
    palpite = int(input('Digite seu palpite: '))
if tentativas < 3:
    print('Parabéns ! Você acertou o número em apenas {} tentativa(s) !'.format(tentativas))
elif 3 < tentativas < 6:
    print('Você acertou o número em {} tentativas'.format(tentativas))
else:
    print('Você precisou de {} tentativas para acertar o número, pelo menos não foram {}..'.format(tentativas, tentativas + 1))