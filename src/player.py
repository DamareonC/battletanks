import os

import pygame

class Player:
    def __init__(self):
        self.surface: pygame.Surface = pygame.image.load(file=os.path.join(os.getcwd(), "res/textures/player.png"))


    def get_surface(self) -> pygame.Surface:
        return self.surface