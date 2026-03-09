entrada = input('\033[mDigite algo: ')
#entrada é um objeto do tipo string
#objeto possui vários métodos (funções) que podem ser utilizados para testar o conteúdo da variável
print ('\033[43mA entrada é alfabética ?\033[m', entrada.isalpha())
print('\033[41mÉ numérico ?\033[m', entrada.isnumeric())
print('\033[42mÉ alfanumérico ?\033[m', entrada.isalnum())
print('\033[40mEstá em maiúsculas ?\033[m', entrada.isupper())
print('\033[44mEstá em minúsculas ?\033[m', entrada.islower())
print('\033[45mEstá capitalizada ?\033[m', entrada.istitle())
print('\033[46mPode ser convertido para número ?\033[m', entrada.isdecimal())
print('\033[47mO tipo primitivo desse valor é\033[m', type(entrada))