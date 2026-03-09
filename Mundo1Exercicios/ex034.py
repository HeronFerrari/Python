salario = float(input('Digite o \033[32msalário\033[m do funcionário: R$ '))
if salario > 1250:
    aumento = salario * 0.10
    print('O funcionário receberá \033[32mR${:.2f}\033[m de aumento, 10% do salário original.'.format(aumento))
else:
    aumento = salario * 0.15
    print('O funcionário receberá \033[32mR${:.2f}\033[m de aumento (15% do salário original).'.format(aumento))

print(f'O salário do funcionário com o \033[32maumento\033[m é R$ {salario + aumento:.2f}.')