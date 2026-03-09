from random import shuffle
print('\033[4mDigite o nome dos quatro alunos:\033[m')
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print ('A \033[36mordem\033[m de apresentação será:')
shuffle(lista)
print ('\033[33m{}\033[m'.format(lista))

#print (sample([aluno1, aluno2, aluno3, aluno4], k=4))
