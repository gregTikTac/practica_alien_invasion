import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("ouutput keys")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event)

