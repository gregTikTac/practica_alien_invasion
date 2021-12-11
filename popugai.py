import pygame


class Poougai():
    """класс для управления попугаем"""

    def __init__(self, popugai_game):
        """нициализация и начальная позиция"""
        self.screen = popugai_game.screen  # для обращения во всех модулях класса
        self.screen_rect = popugai_game.screen.get_rect()  # размещение в нужной позиции



