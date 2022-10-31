import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill("white")
pygame.display.update()


color_yellow = (255, 255, 0)
color_black = (0, 0, 0)
circle(screen, color_yellow, (200, 175), 50)
circle(screen, color_black, (200, 175), 50, 1)
rect(screen, (5, 44, 150), (150, 150, 40, 5))
rect(screen, (5, 44, 150), (215, 150, 40, 5))




pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()