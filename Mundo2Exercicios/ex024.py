opcao = 0
v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digite o segundo número: '))

while opcao != 5:
    opcao = int(input('''    [1] Soma
    [2] Multiplicação
    [3] Maior número
    [4] Novos números
    [5] Sair do programa\nEscolha a operação que deseja realizar: '''))
    if opcao == 1:
        print('A soma entre os números {} e {} é {}'.format(v1, v2, v1 + v2))
    elif opcao == 2:
        print('A multiplicação entre os números {} e {} é {}'.format(v1, v2, v1 * v2))
    elif opcao == 3:
        if v1 > v2:
            print('O maior número é {}'.format(v1))
        elif v2 > v1:
            print('O maior número é {}'.format(v2))
        else:
            print('Os números são iguais')
    elif opcao == 4:
        v1 = int(input('Digite o primeiro número: '))
        v2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        continue
    else:
        print('Opção inválida, tente novamente !')
print('Programa encerrado ')