print('{:=^40}'.format(' LOJA FERRARI '))
preco = float(input('Qual o preço do produto ? R$ '))
juros = preco * 0.20

print('Qual a forma de pagamento ?')
forma = int(input('''[ 1 ] - À vista no dinheiro ou pix
                  \n[ 2 ] - À vista no cartão
                  \n[ 3 ] - Parcelado em até 2x
                  \n[ 4 ] - Parcelado em 3x ou mais\n'''))

if forma == 1:
    total = preco - (preco * 0.10)
    print('O subtotal da sua compra à vista com desconto de 10% é de R$ {:.2f}'.format(total))
elif forma == 2:
    total = preco - (preco * 0.05)
    print('O subtotal da sua compra à vista com cartão é de R$ {:.2f}'.format(total)) 
elif forma == 3:
    total = preco
    print('O subtotal da sua compra parcelada em 2x de R$ {:.2f} é de R$ {:.2f}'.format(preco/2, total))
elif forma == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    total = preco + juros
    print('O subtotal da sua compra parcelada em {}x é de R$ {:.2f}, com total de R$ {:.2f}'.format(parcelas, total/parcelas, total))
else:
    print('Opção de pagamento inválida. Por favor, selecione uma opção entre 1 e 4.')

total = preco
print('Sua compra de R$ {:.2f} irá fica no valor final de R$ {:.2f}.'.format(preco, total))