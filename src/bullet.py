import os
import typing

import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(
        self, x: int | float, y: int | float, angle: int, player_width: int | float
    ):
        super().__init__()

        self.original_image: pygame.Surface = pygame.image.load(
            file=os.path.join(os.getcwd(), "res/textures/bullet.png")
        ).convert_alpha()
        self.image: pygame.Surface = pygame.transform.rotozoom(
            self.original_image, angle, 1
        )
        self.speed: typing.Final[int] = 5
        self.x_speed: int = 0
        self.y_speed: int = 0
        self.updates: int = 180

        match angle:
            case 0:
                self.y_speed = -self.speed
            case 45:
                self.x_speed = -self.speed
                self.y_speed = -self.speed
            case 90:
                self.x_speed = -self.speed
            case 135:
                self.x_speed = -self.speed
                self.y_speed = self.speed
            case 180:
                self.y_speed = self.speed
            case 225:
                self.x_speed = self.speed
                self.y_speed = self.speed
            case 270:
                self.x_speed = self.speed
            case 315:
                self.x_speed = self.speed
                self.y_speed = -self.speed

        self.x_offset: int | float = (
            player_width / 2
            if self.x_speed > 0
            else (-player_width / 2 if self.x_speed < 0 else 0)
        )
        self.y_offset: int | float = (
            player_width / 2
            if self.y_speed > 0
            else (-player_width / 2 if self.y_speed < 0 else 0)
        )

        if self.x_offset != 0 and self.y_offset != 0:
            self.x_offset = self.x_offset / 2
            self.y_offset = self.y_offset / 2

        self.rect: pygame.Rect = self.image.get_rect(
            center=(x + self.x_offset, y + self.y_offset)
        )
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rect.move_ip(self.x_speed, self.y_speed)

        if self.updates > 0:
            self.updates -= 1

        if self.updates == 0:
            self.kill()
