s = 0
cont = 0
for c in range (1,501,2): #(0,500,3) - Menos interações, mas tem que verificar se o múltiplo é par
    if c % 3 == 0:
        print('{} é múltiplo de 3'.format(c))
        #if c % 2 == 0:
        #   print('\033[31m{} é par !\033[m'.format(c))
        #    continue
        print ('Somando {} com {}'.format(s,c))
        s += c
        cont = cont + 1
        print('\033[33mTotal:\033[m {}'.format(s))
print('\033[34mTotal da somatória dos {} números ímpares somados:\033[m {}'.format(cont,s))
