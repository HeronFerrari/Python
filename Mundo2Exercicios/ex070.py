resposta = 'S'
total = acima = menor = cont = 0
print(f'{'LOJA DA LAPA':-^40}')
while resposta[0] == 'S':
    nome = input('Nome do produto: ').strip()
    if nome.isalpha() == False:
        print('Digite letras: ')
        nome = input('Nome do produto: ').strip()
    preco = float(input('Qual o preço do produto: R$ '))
    while preco < 0:
        preco = float(input('Valor inválido\nQual o preço do produto: R$ '))
    if cont == 0 or preco < menor:
        menor = preco
        nomeproduto = nome
    if preco > 1000:
        acima += 1
    total += preco
    resposta = input('Deseja continuar ? [S/N]').strip().upper()
    while resposta[0] != 'S' and resposta[0] != 'N':
        resposta = input('Deseja continuar ? [S/N]').strip().upper()
    cont += 1

print(f'{'FIM DO PROGRAMA':-^40}')
print(f'Total gasto na compra: R${total}')
print(f'Temos {acima} produtos acima de R$ 1000,00 reais')
print(f'Nome do produto comprado com menor preço: {nomeproduto}, R$ {menor}')