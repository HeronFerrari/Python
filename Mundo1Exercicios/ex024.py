cidade = input('Digite o nome de uma \033[32mcidade:\033[m')
cidade = cidade.lower().split()
print('\033[36m{}\033[m'.format('santo' in cidade[0]))