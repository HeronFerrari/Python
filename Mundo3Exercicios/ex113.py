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

def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg).replace(',', '.').strip()
        try:
            valor = float(n)
            ok = True
            break
        except ValueError:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar o número.\033[m')
            return 0
    return valor




inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}')
