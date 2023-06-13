import math
import random
import typing

import pygame

SCREEN_SIZE = (800, 450)  # make sure to keep the 16:9 ratio
PARTICLE_COUNT = 100


class Particle:
    def __init__(self, pos, radius, speed, time_offset, wave_speed) -> None:
        self.pos: typing.List[
            int
        ] = pos  # Use lists instead of tuples because lists are mutable(can be changed after being declared)
        self.radius: int = radius
        self.speed: int = speed
        self.time_offset: int = time_offset
        self.wave_speed: float = wave_speed

    def move(self, dt, time):
        # make the particle go left
        self.pos[0] -= self.speed * dt

        if self.pos[0] < -100:  # particle is out of screen
            self.pos[0] = SCREEN_SIZE[0] + 100

            # if the particle is also too up or down
            if self.pos[1] < -100 or self.pos[1] > SCREEN_SIZE[1] + 100:
                self.pos[1] = random.randint(100, SCREEN_SIZE[1] - 100)

        # Change the Y value
        # NOTE: In pygame y coordinate is flipped so negative Y means up and positive Y means down
        self.pos[1] += math.sin((time + self.time_offset)) * self.wave_speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius)


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.is_running = False
        self.dt = 0
        self.events = []
        self.particles: typing.List[Particle] = []
        self.time = 0
        self.background = pygame.image.load("background.png").convert()
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)

    def run(self):
        self.is_running = True
        self.add_particles()
        while self.is_running:
            pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")
            self.handling_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.dt = self.clock.tick(60) / 18
            self.time += self.dt / 100

    def add_particles(self):
        for _ in range(PARTICLE_COUNT):
            particle = Particle(
                pos=[
                    random.randint(-100, SCREEN_SIZE[0] + 100),
                    random.randint(-100, SCREEN_SIZE[1] + 100),
                ],
                radius=random.randint(2, 4),
                speed=random.randint(6, 12),
                time_offset=random.randint(-4, 3),
                wave_speed=1 + (random.randint(-15, 15) / 10),
            )
            self.particles.append(particle)

    def handling_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                raise SystemExit

    def update(self):
        for particle in self.particles:
            particle.move(self.dt, self.time)

    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.background, (0, 0))

        for particle in self.particles:
            particle.draw(self.screen)


if __name__ == "__main__":
    app = App()
    app.run()
