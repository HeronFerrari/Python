notas = input('Digite as notas do aluno separadas por espaço: ').strip().split()
n1 = float(notas[0])
n2 = float(notas[1])
media = (n1 + n2) / 2

if media < 5.0:
    print('O aluno está \033[31mreprovado\033[m com média {:.1f}.'.format(media))
elif 7 > media >= 5.0:
    print('O aluno está de \033[33mrecuperação\033[m com média {:.1f}.'.format(media))
else:
    print('O aluno está \033[32maprovado\033[m com média {:.1f}.'.format(media))
