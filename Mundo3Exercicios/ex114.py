import ssl
import urllib.request
from ex115.lib.utilidadesCeV import cores

"""Conferir se o site pudim.com.br está funcoinando ou não.
Exercício Python 114: Crie um código em Python que teste se o site pudim.com.br está acessível pelo computador usado.
Dica: para isso, você pode usar a biblioteca urllib."""

url = 'http://pudim.com.br'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ssl._create_unverified_context()) as response:
        print(cores.colorir('Site acessível.', 'verde'))
except urllib.error.URLError as erro:
    print(cores.colorir('Site não acessível.', 'vermelho'))
    print(f'Erro: {erro.reason}')