from random import randint
from time import sleep
numero = randint(0,5)
print('\033[33m' + '-=-'*20 + '\033[m')
print('\033[34mTente adivinhar o número que estou pensando, entre 0 e 5:\033[m')
print('\033[33m' + '-=-'*20 + '\033[m')
chute = int(input('Digite seu chute: '))
print('Procecssando...')
sleep(2)
if chute == numero:
    print('\033[32mPARABÉNS\033[m, você acertou !')
else:
    print('\033[31mQue pena\033[m, não foi dessa vez. O número era {}'.format(numero))