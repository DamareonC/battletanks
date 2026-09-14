import sys
import time
import typing

import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen: pygame.Surface = pygame.display.set_mode(size=(640, 480))

        self.NS_PER_UPDATE: typing.Final[float] = 1000000000.0 / 60.0
        self.last_time_ns: int = time.time_ns()
        self.delta_time: float = 0.0

        self.run()

    def run(self):
        current_time_ns: int

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            current_time_ns = time.time_ns()
            self.delta_time += (current_time_ns - self.last_time_ns) / self.NS_PER_UPDATE
            self.last_time_ns = current_time_ns

            if self.delta_time >= 1:
                self.update()
                self.delta_time -= 1

            self.screen.fill(color=(0, 0, 0))

            self.render()

            pygame.display.flip()

    def update(self):
        pass

    def render(self):
        pass