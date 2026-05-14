from Mundo3Exercicios.ex115.lib.utilidadesCeV.cores import *

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        try:
            valor = int(n)
            ok = True
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar o número.\033[m')
            return 0
        else:
            return valor

def cabecalho(msg, tam=40):
    print(linha(tam))
    print(f'{msg:^{tam}}')
    print(linha(tam))

def linha(tam = 40):
    return '-' * tam

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'{i + 1} - {v}')
    print(linha())
    opc = leiaInt(colorir('Sua opção: ', 'amarelo'))
    return opc