import sys
import time
import typing

import pygame

from player import Player
from spawner import Spawner

SpriteGroup: typing.TypeAlias = pygame.sprite.Group[pygame.sprite.Sprite]


class Game:
    def __init__(self):
        pygame.init()

        self.screen: pygame.Surface = pygame.display.set_mode((640, 480))

        self.player: Player = Player()
        self.bullet_group: SpriteGroup = SpriteGroup()
        self.tank_group: SpriteGroup = SpriteGroup(self.player)

        self.spawner: Spawner = Spawner(self.tank_group, self.bullet_group)

        pygame.display.set_caption("Battletanks")

        self.player.set_bullet_group(self.bullet_group)

        self.run()

    def run(self):
        ns_per_update: typing.Final[float] = 1000000000.0 / 60.0
        last_time_ns: int = time.time_ns()
        delta_time: float = 0.0
        current_time_ns: int

        timer: float | int = time.time()
        updates: int = 0
        frames: int = 0

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
                updates += 1

            self.screen.fill((64, 64, 64))

            self.render()
            frames += 1

            pygame.display.flip()

            if time.time() - timer > 1:
                timer += 1
                pygame.display.set_caption(f"Battletanks | {updates}ups, {frames}fps")
                updates = 0
                frames = 0

    def update(self):
        self.bullet_group.update()
        self.tank_group.update()

        self.spawner.update()

    def render(self):
        self.bullet_group.draw(self.screen)
        self.tank_group.draw(self.screen)
