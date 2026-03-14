peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura **2)

print('O seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está \033[31mabaixo do peso\033[m.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso \033[32mideal\033[m.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com \033[33msobrepeso\033[m.'.format(imc))
elif 40 > imc >= 30: #Forma alternativa de escrever a condição, sem operador lógico
    print('Você está com \033[31mobesidade\033[m.'.format(imc))
else:
    print('Você está com \033[36mobesidade mórbida\033[m.'.format(imc))