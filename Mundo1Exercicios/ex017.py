import math
oposto = float(input('Digite o comprimento do cateto oposto em cm:'))
adjacente = float(input('Digite o comprimento do cateto adjacente em cm:'))
hipotenusa = math.hypot(oposto, adjacente)
print('A \033[36mhipotenusa\033[m irá medir \033[37m{:.2f} cm\033[m'.format(hipotenusa))
#Soma dos quadrados dos catetos é igual ao quadrado da hipotenusa