import random
print('\033[37mEscreva os nomes dos alunos:\033[m')
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno \033[36mescolhido\033[m foi \033[33m{}\033[m'.format(random.choice(lista)))