import pygame
import sys
from settings import Settings
from popugai import Popugai


class InitPractica():
    """класс для упраления русурсами и поведением игры"""

    def __init__(self):
        """инициализирует угру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # атрибуты для создания экрана
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Практика")  # верхня часть окна с названием
        self.popugai = Popugai(self)  # создание экземпляра

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()  # вызов вспомогательного _метода
            self._update_screen()  # вызов вспомогательного _метода
            self.popugai.update() # вызов из клааса попугай для обновления позиции на экране

    def _check_events(self):
        for event in pygame.event.get():  # отслеживание событий клавиатуры и мыши
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # при обнаружении события keydown проверяем нажата ли клавиша
                if event.key == pygame.K_RIGHT:
                    self.popugai.moving_right = True # начинается непрерывное движение
                elif event.key == pygame.K_LEFT:
                    self.popugai.moving_left = True

            elif event.type == pygame.KEYUP:  # если клавиша отжата
                if event.key == pygame.K_RIGHT:
                    self.popugai.moving_right = False  # движение прекращается
                elif event.key == pygame.K_LEFT:
                    self.popugai.moving_left = False
    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)  # при кажд проходе цикла переписывает экран(для получения цвета фона)
        self.popugai.blitme()
        pygame.display.flip()  # отображение последнего прорисованного экрана


if __name__ == "__main__":
    game_pr = InitPractica()  # экземпляр игры
    game_pr.run_game()  # вызов метода
