def ficha(nome='Desconhecido', gols=0):
    """Exibe a ficha de um jogador de futebol.
    :param nome: O nome do jogador (padrão: 'Desconhecido').
    :param gols: O número de gols marcados (padrão: 0)."""
    if nome.strip() == '':
        nome = 'Desconhecido'
    if gols == '' or gols == ' ' or gols.isalpha():
        gols = 0
    print(f'O jogador {nome.strip()} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ').capitalize()
gols = input('Número de gols: ')

ficha(nome, gols)