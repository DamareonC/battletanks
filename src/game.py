import sys
import time
import typing

import pygame

from player import Player


class Game:
    def __init__(self):
        pygame.init()

        self.screen: pygame.Surface = pygame.display.set_mode(size=(640, 480))

        self.player: Player = Player()
        self.sprite_group = pygame.sprite.Group(self.player)

        pygame.display.set_caption("Battletanks")

        self.run()

    def run(self):
        ns_per_update: typing.Final[float] = 1000000000.0 / 60.0
        last_time_ns: int = time.time_ns()
        delta_time: float = 0.0
        current_time_ns: int

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            current_time_ns = time.time_ns()
            delta_time += (current_time_ns - last_time_ns) / ns_per_update
            last_time_ns = current_time_ns

            if delta_time >= 1:
                self.update()
                delta_time -= 1

            self.screen.fill(color=(64, 64, 64))

            self.render()

            pygame.display.flip()

    def update(self):
        self.sprite_group.update()

    def render(self):
        self.sprite_group.draw(self.screen)
