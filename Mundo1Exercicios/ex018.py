import math
angulo = int(input('\033[35mDigite um ângulo qualquer:\033[m'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem:\n\033[36mSeno\033[m de {:.2f}'.format(angulo, seno))
print('\033[34mCosseno\033[m de {:.2f}\n\033[33mTangente\033[m de {:.2f}'.format(cosseno, tangente))
