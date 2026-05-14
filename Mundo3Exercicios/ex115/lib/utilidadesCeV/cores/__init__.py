def colorir(texto, letra='branco', fundo = None):
    txt = {
        'preto': 30,  # 0 Preto
        'vermelho': 31,  # 1 Vermelho
        'verde': 32,  # 2 Verde
        'amarelo': 33,  # 3 Amarelo
        'azul': 34,  # 4 Azul
        'roxo': 35,  # 5 Roxo
        'ciano': 36,  # 6 Ciano
        'branco': 37   # 7 Branco
    }

    bg = {
        'preto': 40,  # 0 Preto
        'vermelho': 41,  # 1 Vermelho
        'verde': 42,  # 2 Verde
        'amarelo': 43,  # 3 Amarelo
        'azul': 44,  # 4 Azul
        'roxo': 45,  # 5 Roxo
        'ciano': 46,  # 6 Ciano
        'branco': 47   # 7 Branco
    }


    c_letra = txt.get(letra.lower(), 37)  # Padrão para branco

    if fundo:
        c_fundo = bg.get(fundo.lower(), 40)  # Padrão para preto
        return f'\033[0;{c_letra};{c_fundo}m{texto}\033[m'    
    else:
        return f'\033[0;{c_letra}m{texto}\033[m'