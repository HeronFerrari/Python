from lib.utilidadesCeV.cores import *
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize().strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print(colorir('Pessoa cadastrada com sucesso!', 'verde'))
    elif resp == 3:
        print(colorir('Sistema finalizado. Obrigado, volte sempre!', 'amarelo'))
        break
    else:    
        print(colorir('Opção inválida. Tente novamente.','vermelho'))
        sleep(2)
        continue

