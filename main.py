#/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import webbrowser
import random
import pygame
import time

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

i = 1

while True:
    if i == 1:
        window.blit(pygame.image.load('1.png'), (0, 0))
        pygame.display.update()
    elif i == 2:
        window.blit(pygame.image.load('2.png'), (0, 0))
        pygame.display.update()
    elif i == 3:
        window.blit(pygame.image.load('3.png'), (0, 0))
        pygame.display.update()
    elif i == 4:
        window.blit(pygame.image.load('4.png'), (0, 0))
        pygame.display.update()

    sites = random.choice(['https://www.youtube.com/watch?v=dQw4w9WgXcQ','https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
    visit = format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1,2)
    time.sleep(seconds - 0.9)

    if i == 5:
        i = 1
    else:
        i = i + 1