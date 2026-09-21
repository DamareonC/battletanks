import os
import typing

import pygame

from bullet import Bullet
from player import Player

SpriteGroup: typing.TypeAlias = pygame.sprite.Group[pygame.sprite.Sprite]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: int | float, y: int | float, bullet_group: SpriteGroup):
        super().__init__()

        self.original_image: pygame.Surface = pygame.image.load(
            os.path.join(os.getcwd(), "res/textures/enemy.png")
        ).convert_alpha()
        self.image: pygame.Surface = self.original_image
        self.rect: pygame.Rect = self.image.get_rect()
        self.bullet_group: SpriteGroup = bullet_group
        self.rect.x = x
        self.rect.y = y

    def update(self):
        sprite: pygame.sprite.Sprite | None = pygame.sprite.spritecollideany(self, self.bullet_group)

        if sprite and isinstance(sprite, Bullet):
            bullet: Bullet = sprite

            if isinstance(bullet.get_owner(), Player):
                self.kill()
                bullet.kill()
