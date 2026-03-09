valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Digite em quantos anos o comprador irá pagar a casa: '))
limite = salario * 0.30
prestacao = valor / (anos*12)

print('Valor da prestação em {} anos: {} vezes de R$ {:.2f}'.format(anos, anos*12, prestacao))
print('Limite de 30% do salário do comprador: R$ {:.2f}'.format(limite))

if prestacao > limite:
    print('O empréstimo no valor de R$ {:.2f} foi \033[31mnegado\033[m, pois excede o limite de 30% do salário do comprador.'.format(valor))
else:
    print('O financiamento foi \033[32maprovado !\033[m O valor da prestação mensal será de R$ {:.2f}'.format(prestacao))