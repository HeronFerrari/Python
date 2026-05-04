from time import sleep
c = ('\033[0;30;41m', #0 Vermelho
     '\033[0;30;42m', #1 Verde
     '\033[0;30;43m', #2 Amarelo
     '\033[0;30;44m', #3 Azul
     '\033[0;30;45m', #4 Roxo
     '\033[0;30;46m', #5 Ciano
     '\033[0;30;47m') #6 Branco

def linha(msg, cor=0):
    """Exercício 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
    :param msg: A mensagem a ser exibida.
    :param cor: A cor do texto (0 para padrão).
    """
    tracos = '-' * (len(msg) + 4)
    print(f'{c[cor]}{tracos}\033[m')
    print(f'{c[cor]}  {msg}  \033[m')
    print(f'{c[cor]}{tracos}\033[m')

def ajuda(comando):
    linha(f"Acessando o manual do comando '{comando}'", cor=5)
    sleep(2)
    
    # 1. "Liga" a cor antes do help (ex: 7;30m inverte as cores, deixando fundo branco e letra preta)
    print(f'{c[6]}') 
    
    # 2. Chama o help (ele vai imprimir direto na tela, aproveitando a cor ligada acima)
    help(comando)
    
    sleep(1)
    # 3. "Desliga" a cor para não manchar o resto do terminal
    print('\033[m')

while True:
    linha('SISTEMA DE AJUDA PYHELP', cor=1)
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
    
sleep(2)
linha('Encerrando o PYHELP... Até logo!', cor=0)