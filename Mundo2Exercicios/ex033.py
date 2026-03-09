from random import randint
venceu = 1
tentativa = escolha = 0

print('Vamos jogar par ou ímpar ?')

#Enquanto jogador não vence a variável fica nula
while venceu:
    escolha = str(input('Ímpar ou par [I/P] ? ')).strip().upper()
    while escolha[0] not in 'IiPp':
        print('Por favor, digite i para ímpar ou p para par.')
        escolha = str(input('Ímpar ou par [I/P] ? ')).strip().upper()
    computador = randint(0,10)
    if 'I' in escolha[0]:
        escolha = 'Impar' 
    elif 'P' in escolha[0]:
        escolha = 'Par'
    jogador = int(input('Digite seu número: '))
    soma = computador + jogador
    print('=-' * 50)
    if soma % 2 == 0: #Se soma deu par verifico se a escolha foi par
        if 'I' in escolha[0]: #Se diferente de 0 então é ímpar, logo perdeu
            print(f'Computador: {computador}\nVocê: {jogador}\nVocê escolheu \033[31m{escolha}\033[m, a soma foi \033[34mPar\033[m, então você \033[31mperdeu\033[m')
            venceu = 0
        else: #Senão tem valor então é zero, logo venceu
            tentativa += 1
            print(f'Você venceu com Par, vamos novamente !')
    else:
        if 'I' in escolha[0]:
            tentativa += 1
            print(f'Você venceu com Ímpar, vamos novamente !')
        else:
            print(f'Computador:{computador}\nVocê:{jogador}\nVocê escolheu \033[34m{escolha}\033[m, a soma foi \033[31mÍmpar\033[m, então você \033[31mperdeu\033[m')
            venceu = 0

if tentativa > 0:
    print(f'Parabéns, você venceu {tentativa} vezes')
else:
    print(f'Você não ganhou nenhuma vez, tente novamente !')