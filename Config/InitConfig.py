import pygame


class InitConfig:
    # variables
    clock = None
    windowSize = None
    screen = None

    # constructor
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.windowSize = (400, 400)

        pygame.init()
        pygame.display.set_caption('My Pygame')

        self.screen = pygame.display.set_mode(self.windowSize, 0, 32)

    # methods
