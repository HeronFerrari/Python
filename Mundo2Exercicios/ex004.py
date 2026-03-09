from datetime import date
nascimento = int(input('Digite o ano de seu nascimento com quatro algarismos '))
print('Analisando o ano de seu nascimento:'.format(nascimento))

if date.today().year - nascimento == 18:
    print('Você completa 18 anos este ano, você precisa se alistar no serviço militar obrigatório.')
elif date.today().year - nascimento < 18:
    print('Você ainda não tem 18 anos completos este ano, você precisa se alistar no serviço militar obrigatório daqui a {} anos'.format(18 - (date.today().year - nascimento)))
else:
    print('Você já tem mais de 18 anos completos este ano, você deveria ter se alistado no seviço militar obrigatório há {} anos, em {}.'.format(date.today().year - nascimento - 18, nascimento + 18))