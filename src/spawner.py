import random
import typing

import pygame

from enemy import Enemy

SpriteGroup: typing.TypeAlias = pygame.sprite.Group[pygame.sprite.Sprite]


class Spawner:
    def __init__(self, tank_group: SpriteGroup, bullet_group: SpriteGroup):
        self.tank_group: SpriteGroup = tank_group
        self.bullet_group: SpriteGroup = bullet_group

    def update(self):
        if random.randrange(600) == 0:
            x: int = random.randrange(0, 640 - 64)
            y: int = random.randrange(0, 480 - 64)
            enemy: Enemy = Enemy(x, y, self.bullet_group)

            self.tank_group.add(enemy)
