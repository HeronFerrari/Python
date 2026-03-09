distancia = int(input('Qual a distância da sua viagem em \033[31mkm\033[m ? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem é de \033[1;37;42mR$ {:.2f}\033[m'.format(preco))