from time import sleep
metros = float(input('\033[33mDigite uma quantidade de metros: \033[m'))
print('\033[1;47m' + '-'*40,'Convertendo', '-'*40+'\033[m')
sleep(2)
print (' {:4} \033[33mMetros\033[m equivalem a: \n {} \033[32mDecímetros\033[m \n {} \033[31mCentímetros\033[m \n {} \033[34mMilímetros\033[m'.format(metros, metros * 10, metros * 100, metros * 1000))
print ('{:4} \033[35mDecâmetros\033[m \n {} \033[36mHectômetros\033[m \n {} \033[37mQuilômetros\033[m'.format(metros / 10, metros / 100, metros / 1000))