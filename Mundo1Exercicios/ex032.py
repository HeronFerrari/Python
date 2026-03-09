from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print( 'O ano {} é \033[32mbissexto\033[m.'.format(ano))
        else:
            print('O ano {} \033[31mnão é bissexto\033[m.'.format(ano))
    else:
        print( 'O ano {} é \033[32mbissexto\033[m.'.format(ano))
else:
    print('O ano {} \033[31mnão é bissexto\033[m.'.format(ano))