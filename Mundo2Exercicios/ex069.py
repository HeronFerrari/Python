resposta = 'S'
pessoasmaiores = 0
homens = 0
mulheresmenores = 0
while resposta == 'S':
    idade = int(input('Qual sua idade ? '))
    while idade > 135 or idade < 0:
        print('Digite uma idade válida: ', end='')
        idade = int(input(''))
    if idade >= 18:
        pessoasmaiores += 1
    sexo = input(('Qual seu sexo ? [M/F] ')).strip().upper()
    while sexo[0] != 'M' and sexo[0] != 'F':
        print('Digite [M/F] para escolher o sexo: ',end='')
        sexo = input(('')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenores += 1  

    resposta = input(('Pessoa cadastrada, deseja continuar ? [S/N]')).strip().upper()
    
    while 'N' != resposta[0] != 'S':
        print('Digite Sim ou não apenas: ',end='')
        resposta = input('').strip().upper()
    
print(f'HÁ {pessoasmaiores} pessoas maiores de 18 anos\nHÁ {homens} homens cadastrados\nHÁ {mulheresmenores} mulheres com menos de 20 anos\n')