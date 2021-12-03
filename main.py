import pygame
import sys
from core.character import Character

pygame.init()
screen = pygame.display.set_mode((800, 600))

group = pygame.sprite.Group()

ingrid = Character('resources/imgs/Ingrid.png')

group.add(ingrid)

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    group.update()
    screen.fill((0, 0, 0))
    group.draw(screen)
    pygame.display.update()
    clock.tick(6)
