numero = int(input('\033[33mDigite um número: \033[m'))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print ( ' Análise do número {}. \n O \033[31mdobro\033[m é {}. \n O \033[32mtriplo\033[m é {}. \n A \033[34mraiz quadrada\033[m é {:.3f}.'.format(numero, dobro, triplo, raiz))
# Interessante utilizar a mesma variável n para dobro, triplo e raiz, para economizar memória caso não seja usado em outros cálculos