def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a:.2f}m²')

def linha(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


linha('Controle de terrenos')
area(float(input(f'Largura (m): ')), float(input('Comprimento (m): ')))