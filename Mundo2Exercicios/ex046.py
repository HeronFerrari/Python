from time import sleep
import emoji
for c in range (10,0,-1):
    print("{}..".format(c))
    sleep(1)
print(emoji.emojize(":fireworks::red_heart:   {} :red_heart: :fireworks:").format('Feliz Ano Novo !'))