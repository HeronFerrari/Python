preco = float(input('\033[33mDigite o preço de um produto:\033[m'))
novo = preco - (preco * 0.05)
print('O preço do produto com desconto de 5% é de \033[32mR$ {:.2f}.\033[m'.format(novo))