from datetime import date
nascimento = str(input('Digite seu ano de nascimento com quatro algarismos para o ano: '))

data_atual = date.today()
idade = data_atual.year - int(nascimento)
if idade <= 9:
    print('O atleta tem {} anos e é \033[32mmirim\033[m.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e é \033[32minfantil\033[m.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e é \033[32mjúnior\033[m.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e é \033[34msênior\033[m.'.format(idade))
else:
    print('O atleta tem {} anos e é \033[34mmaster\033[m.'.format(idade))
    
