
def escreva(msg):
    print('~'*(len(msg)+2))
    print(f'{msg:^{len(msg)+2}}')
    print('~'*(len(msg)+2))


escreva(input('Digite uma mensagem: ').capitalize())
escreva('Viu só ?')
escreva('É fácil de fazer isso !')