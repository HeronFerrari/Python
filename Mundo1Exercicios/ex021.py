import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
input('Pressioner \033[32mENTER\033[m para iniciar a música')
pygame.mixer.music.play()
input('Pressioner \033[31mENTER\033[m para parar a música')
pygame.mixer.music.stop()