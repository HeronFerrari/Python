from time import sleep


def linha(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

def contador(inicio, fim, passo):
    
    if passo == 0:
        linha(f'Contagem de {inicio} a {fim} de {1} em {1}')
    else:
        linha(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
    if inicio > fim:
        if passo > 0:
            passo *= -1
        elif passo == 0:
            passo = -1
        for c in range(inicio, fim-1, passo):
            print(c, end=' ', flush=True)
            sleep(0.3)
    elif inicio == fim:
            return print('O início e fim são iguais, não é possível realizar a contagem ! ')
    else:
        if passo == 0:
            passo = 1
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.3)
        

    print('FIM !')



contador(1,10,1)
contador(10,1,1)
print('Agora é sua vez de personalizar a contagem !')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)