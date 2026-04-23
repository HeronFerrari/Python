nome = str(input('Digite seu nome: ')).strip().capitalize()
aluno = {'nome': nome}
media = float(input(f'Digite a média do aluno {aluno["nome"]}: '))
aluno['media'] = media
aluno['situacao'] = 'Aprovado' if media >= 7 else 'Reprovado'

print(f'Média do aluno {aluno["nome"]} é {aluno["media"]}.')
print(f'Situação do aluno {aluno["nome"]} é {aluno["situacao"]}.')
