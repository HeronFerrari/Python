from datetime import date
nome = str(input('Digite seu nome: ')).strip()
ano = int(input('Digite o ano de nascimento: '))
carteira = int(input('Digite o número da carteira de trabalho (0 se não tiver): '))
dict = {'Nome': nome, 'Idade': date.today().year- ano, 'Carteira de Trabalho': carteira}
if carteira > 0:
    ano_contratacao = int(input('Digite o ano de contratação: '))
    salario = float(input('Digite o salário: '))
    dict['Ano de contratação'] = ano_contratacao
    dict['Salário'] = salario
    dict['Aposentadoria'] = ano_contratacao + 35 - ano

print(dict)

for k,v in dict.items():
    print(f'{k} tem o valor {v}')