numero = int(input('Digite um número inteiro: '))
print('A tabuada de {} é:'.format(numero))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m'}

for c in range (0,10):
    print('{}{}{} x {}{:>2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], c + 1, cores['limpa'], cores['verde'], numero * (c + 1), cores['limpa']))