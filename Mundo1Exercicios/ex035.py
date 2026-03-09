from time import sleep
retas = str(input('Digite o \033[34mcomprimento de três retas\033[m separadas por espaços: ')).strip().split()
a, b, c = map(float, retas)
print('Analisando as retas: {}, {} e {}'.format(a, b, c))
sleep(2.5)
if a + b > c and a + c > b and b + c > a:
    print('As retas \033[32mpodem formar um triângulo\033[m :)')
else:
    print('As retas \033[31mnão podem formar um triângulo\033[m :(')