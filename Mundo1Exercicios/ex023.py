numero = int(input('Digite um número entre \033[37m0 e 9999:\033[m'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('\033[34mUnidade:\033[m {:>}'.format(u))
print('\033[34mDezena:\033[m {:>}'.format(d))
print('\033[34mCentena:\033[m {:>}'.format(c))
print('\033[34mMilhar:\033[m {:>}'.format(m))
