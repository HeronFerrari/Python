times = ('São Paulo', 'Palmeiras', 'Fluminense', 'Bahia', 'Bragantino', 'Flamengo', 'Coritiba',
         'Athletico-PR', 'Grêmio', 'Corinthians', 'Mirassol', 'Chapecoense', 'Atlético-MG',
          'Santos', 'Vasco da Gama', 'EC Vitória', 'Botafogo', 'Remo', 'Internacional', 'Cruzeiro')

print(f'{'Início da tabela':-^30}')

c = 0
for time in times:
    c = c+1
    if c > 5:
        break
    print(f"{c}º",end=' ')
    print(time)
    # Ou print(times[0:5]) sem o for.

print(f'{'Fim da tabela':-^30}')

ultimos = times[16:21] # Últimos times do campeonato, note que nesse tipo de fatiamento no meio da string, é desconsiderado o começo também.
for c in range(0,4): #Sem break utilziando for padrão com range.
      print(f'{c+17}º {ultimos[c]}') # Ou print(ultimos) sem o for.


print(f'{'Tabela em ordem alfabética':-^30}')
for c in range(0,20):
    print(f'{c+1}º',sorted(times)[c]) #Printando igual uma tabela

for pos, time in enumerate(times):
    if time == "Chapecoense":
        chape = pos+1

print(f'O Chapecoense está na {chape}ª posição no campeonato')

print('\nPrograma finalizado')