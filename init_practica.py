import pygame
import sys


class InitPractica():
    """класс для упраления русурсами и поведением игры"""

    def __init__(self):
        """инициализирует угру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))  # размер экрана
        pygame.display.set_caption("Практика")  # верхня часть окна с названием



