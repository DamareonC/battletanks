import os

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: int | float, y: int | float):
        super().__init__()

        self.original_image: pygame.Surface = pygame.image.load(
            file=os.path.join(os.getcwd(), "res/textures/enemy.png")
        ).convert_alpha()
        self.image: pygame.Surface = self.original_image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
