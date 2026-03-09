numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print(' O sucessor do número {}{}{} é {}{}{}, e seu antecessor é {}{}{}.'.format('\033[0;32;43m', numero, '\033[m', '\033[44m', sucessor, '\033[m', '\033[41m', antecessor, '\033[m'))