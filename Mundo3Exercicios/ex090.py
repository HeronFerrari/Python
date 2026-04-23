nome = str(input('Digite seu nome: ')).strip().capitalize()
aluno = {'Nome': nome}
media = float(input(f'Digite a média do aluno {aluno["Nome"]}: '))
aluno['Media'] = media
aluno['Situacao'] = 'Aprovado' if media >= 7 else 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}.')