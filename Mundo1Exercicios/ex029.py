velocidade = int(input('Qual a \033[34mvelocidade\033[m do carro ? '))
if velocidade > 80:
    print('Você foi \033[31mmultado\033[m por excesso de velocidade !')
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('\033[32mParabéns\033[m, você está dentro do limite de velocidade !')