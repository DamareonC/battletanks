import os

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.original_image: pygame.Surface = pygame.image.load(
            file=os.path.join(os.getcwd(), "res/textures/player.png")
        ).convert_alpha()
        self.image: pygame.Surface = self.original_image
        self.rect: pygame.Rect = self.image.get_rect()
        self.speed: int = 2
        self.angle: int = 0

    def update(self):
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.angle = 0
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.angle = 180

        if keys[pygame.K_a]:
            self.rect.x -= self.speed

            if keys[pygame.K_w]:
                self.angle = 45
            elif keys[pygame.K_s]:
                self.angle = 135
            else:
                self.angle = 90
        elif keys[pygame.K_d]:
            self.rect.x += self.speed

            if keys[pygame.K_w]:
                self.angle = 315
            elif keys[pygame.K_s]:
                self.angle = 225
            else:
                self.angle = 270

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
