nome = input('Digite seu \033[32mnome completo:\033[m ').strip()
print('\033[34mPrimeiro nome:\033[m {}'.format(nome.split()[0]))
print('\033[31mÚltimo nome:\033[m {}'.format(nome.split()[len(nome.split())-1]))