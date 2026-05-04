def linha(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

def maior(*num):
    maior = menor = 0
    linha('Analisando os valores passados...')
    for c in range(len(num)):
        if c == 0:
            maior = menor = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
            if num[c] < menor: 
                menor = num[c]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'Os valores são: {num}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

         