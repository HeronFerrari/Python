def voto(ano_nascimento):
    from datetime import date #Economiza memória, pois só será usada dentro da função
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    while ano_nascimento < 0 or ano_nascimento > ano_atual:
        print('Ano de nascimento inválido. Tente novamente.')
        ano_nascimento = int(input('Em que ano você nasceu ? '))
        idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

    

ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))