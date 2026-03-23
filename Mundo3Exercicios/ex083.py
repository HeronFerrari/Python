expressao = str(input('Digite uma expressão matemática: ')).strip()
pilha = []

for l in expressao:
    if l == '(':
        pilha.append('(')
    elif l == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão \033[32mválida\033[m ! ')
else:
    print('Expressão \033[31minválida\033[m !')

