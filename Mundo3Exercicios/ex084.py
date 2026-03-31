pessoas = list()
dados = []
pesados = []
leves = []
total = pesos = 0

while True:
    dados.append(str(input('Qual seu nome:')))
    dados.append(float(input('Qual seu peso:')))
    total +=1
    pessoas.append(dados[:])
    dados.clear()
    resposta = input('Deseja continuar ? [S/N] ').strip().upper()
    if resposta != 'S':
        break

for p in pessoas:
    pesos += p[1]

media = pesos/total

for p in pessoas:
    if p[1] > media:
        pesados.append(p)
    else:
        leves.append(p)

print('-'*30)
print(f'Total de pessoas cadastradas: {total}')
print('-'*30)
print(f'Média de peso: {pesos/total:.2f}')
print('-'*30)
print('Divisão de peso conforme a média obtida')
print('-'*30)
print(f'Lado dos mais pesados {pesados}')
print('-'*30)      
print(f'Lado dos mais leves {leves}')