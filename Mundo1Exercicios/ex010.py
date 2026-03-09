reais = float(input('\033[33mDigite o valor em reais que você possui na carteira:\033[mR$'))
dolares = reais / 5.25
print('Cotação atual do dólar: \033[34mUS$ 5,25\033[m')
print('Com \033[32mR$\033[m {:.2f} você pode comprar \033[34mUS$\033[m {:.2f} dólares.'.format(reais, dolares))