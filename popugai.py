import pygame


class Popugai():
    """класс для управления попугаем"""

    def __init__(self, popugai_game):
        """нициализация и начальная позиция"""
        self.screen = popugai_game.screen  # для обращения во всех модулях класса
        self.screen_rect = popugai_game.screen.get_rect()  # размещение в нужной позиции

        # загрузка изображения
        self.image = pygame.image.load('images/popug.bmp')  # загрузка изображения попугая
        self.rect = self.image.get_rect()  # размещение на поверхности окна изображения попугая
        # каждый новый попугай появляется у нижнего края платформы
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False  # флаг перемещения

    def update(self):
        """Обновление позиции попугая"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):  # метод, который выводит изображения на экран в прзиции self.rect
        """Рисует попугая в текущей позиции"""
        self.screen.blit(self.image, self.rect)