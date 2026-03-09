nome = input('Digite seu \033[32mnome completo:\033[m ').strip()
nome = nome.lower()
print('\033[35m{}\033[m'.format('silva' in nome))