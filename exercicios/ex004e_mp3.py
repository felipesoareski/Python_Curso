import pygame

pygame.init()

pygame.mixer.music.load('ex004.mp3')
pygame.mixer.music.play()

input()
pygame.event.wait()