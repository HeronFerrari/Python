numero = int(input('\033[4mDigite um número inteiro:\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m'}

print('\033[4mAqui está a tabuada do número {}:\033[m'.format(numero))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 1,cores['limpa'], cores['verde'], numero * 1, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 2,cores['limpa'], cores['verde'], numero * 2, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 3,cores['limpa'], cores['verde'], numero * 3, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 4,cores['limpa'], cores['verde'], numero * 4, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 5,cores['limpa'], cores['verde'], numero * 5, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 6,cores['limpa'], cores['verde'], numero * 6, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 7,cores['limpa'], cores['verde'], numero * 7, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 8,cores['limpa'], cores['verde'], numero * 8, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 9,cores['limpa'], cores['verde'], numero * 9, cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'],numero,cores['limpa'], cores['amarelo'], 10,cores['limpa'], cores['verde'], numero * 10, cores['limpa']))