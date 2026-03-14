from datetime import date
atual = date.today().year
maior = 0
menor = 0 

for c in range(0,7):
    ano = int(input('Digite o ano de nascimento da {} pessoa: '.format(c+1)))
    if atual - ano >=18:
        print('A pessoa {} é \033[32mmaior de idade\033[m, tem {} anos'.format(c+1, atual - ano))
        maior += 1
    else:
         print('A pessoa {} é \033[31mmenor de idade\033[m, tem {} anos'.format(c+1, atual - ano))
         menor += 1
print('{} Pessoas são \033[31mmenores de idade\033[m e {} são \033[32mmaiores de idade\033[m'.format(maior,menor))
    