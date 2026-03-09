from time import sleep
retas = str(input('Digite o \033[34mcomprimento de três retas\033[m separadas por espaços: ')).strip().split()
a = float(retas[0])
b = float(retas[1])
c = float(retas[2])
print('Analisando as retas: {}, {} e {}'.format(a, b, c))
sleep(2.5)
if a + b > c and a + c > b and b + c > a:
    print('As retas \033[32mpodem formar um triângulo\033[m')
    if a == b == c:
        print('As retas formam um \033[32mtriângulo equilátero\033[m.')
    elif a == b or a == c or b == c:
        print('As retas formam um \033[33mtriângulo isósceles\033[m.')
    else:
        print('As retas formam um \033[34mtriângulo escaleno\033[m.')
else:
    print('As retas \033[31mnão podem formar um triângulo\033[m :(') 