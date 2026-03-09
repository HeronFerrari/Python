temperatura = float(input('\033[1mDigite a temperatura em °C:\033[m'))
farenheit = temperatura * 1.8 + 32
print('A temperatura de \033[34m{:.2f}°C\033[m corresponde a \033[32m{:.2f}°F.\033[m'.format(temperatura, farenheit))