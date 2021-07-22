import sys
import pygame
from pygame import QUIT

from Config.InitConfig import InitConfig


class MainLoop:

    def __init__(self):
        self.initConfig = InitConfig()
        self.player_rec = pygame.Rect(50, 50, 100, 100)

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        pygame.draw.rect(self.initConfig.screen, (255, 0, 0), self.player_rec)

        pygame.display.update()
        self.initConfig.clock.tick(60)
