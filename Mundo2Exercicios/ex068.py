from random import randint
venceu = 1
tentativa = 0
escolha = ' '
print('Vamos jogar par ou ímpar ?')

#Enquanto jogador não vence a variável fica nula
while venceu:
    escolha = str(input('Por favor, digite [I] para ímpar ou [P] para par. ')).strip().upper()[0]
    while escolha not in 'IP':
        escolha = str(input('Por favor, digite [I] para ímpar ou [P] para par. ')).strip().upper()[0]
    computador = randint(0,10)
    jogador = int(input('Digite seu número: '))
    soma = computador + jogador
    print(f'Computador:{computador}\nVocê:{jogador}')
    if escolha == 'I':
        if soma % 2 == 0:
            print(f'Você escolheu \033[31m{escolha}\033[m, a soma {soma} é \033[34mPar\033[m, então você \033[31mperdeu\033[m')
            venceu = 0
        else:
            tentativa += 1
            print(f'A soma {soma} é \033[31mÍmpar\033[m, você venceu !\nVamos novamente !')
    elif escolha == 'P':
        if soma % 2 == 1:
            print(f'Você escolheu \033[34m{escolha}\033[m, a soma {soma} é \033[31mÍmpar\033[m, então você \033[31mperdeu\033[m')
            venceu = 0
        else:
            tentativa += 1
            print(f'A soma {soma} é \033[34mPar\033[m, você venceu !\nVamos novamente !')
    print('=-' * 50)
if tentativa > 0:
    print(f'Parabéns, você venceu {tentativa} vezes')
else:
    print(f'Você não ganhou nenhuma vez, tente novamente !')