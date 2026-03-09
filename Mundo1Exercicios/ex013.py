salario = float(input('\033[33mDigite o seu salário em reais:\033[m'))

print('Salário anterior: \033[31mR${:.2f}\033[m \nAumento de 15%: \033[32mR${:.2f}\033[m \nSeu novo salário com 15% de aumento será de \033[32mR$ {:.2f}.\033[m'.format(salario, salario * 0.15, salario * 1.15))