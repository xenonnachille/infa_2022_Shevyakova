import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill("white")
pygame.display.update()


color_yellow = (255, 255, 0)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
circle(screen, color_yellow, (200, 175), 50)
circle(screen, color_black, (200, 175), 50, 1)
circle(screen, color_red, (178, 157), 8)
circle(screen, color_black, (178, 157), 4)
circle(screen, color_red, (223, 158), 10)
circle(screen, color_black, (223, 158), 5)

polygon(screen, color_black, [(150,132), (189,152), (150,132)], 5)
polygon(screen, color_black, [(205, 155), (250, 122), (205, 155)], 6)
rect(screen, color_black, (178, 175, 223-178, 7))






pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()