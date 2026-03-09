altura = float(input('\033[7mDigite a altura da sua parede em metros:\033[m'))
largura = float(input('\033[7mDigite a largura da sua parede em metros:\033[m'))
area = altura * largura
tinta = area / 2
print (' A \033[33márea\033[m da parede é de {:.2f} \033[31mmetros quadrados\033[m. \n Para pintar essa parede, serão necessários {:.2f} \033[32mlitros de tinta.\033[m'.format(area, tinta))