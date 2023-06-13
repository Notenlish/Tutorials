import random
import typing

import pygame

SCREEN_SIZE = (800, 600)
PARTICLE_COUNT = 100


class Particle:
    def __init__(self, pos: typing.List[int], radius: int, speed: int) -> None:
        # Use lists instead of tuples because lists are mutable(can be changed after being declared)
        self.pos = pos
        self.radius = radius
        self.speed = speed

    def update(self, dt):
        # make the particle go left
        self.pos[0] -= self.speed * dt
        if self.pos[0] < -100:  # particle is out of screen
            self.pos[0] = SCREEN_SIZE[0] + 100

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius)


class ParticleManager:
    def __init__(self) -> None:
        self.particles: typing.List[Particle] = []

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def add_particles(self):
        for _ in range(PARTICLE_COUNT):
            particle = Particle(
                pos=[
                    random.randint(-100, SCREEN_SIZE[0] + 100),
                    random.randint(-100, SCREEN_SIZE[1] + 100),
                ],
                radius=random.randint(3, 6),
                speed=random.randint(4, 8),
            )
            self.particles.append(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.is_running = False
        self.dt = 0
        self.events = []
        self.particle_manager = ParticleManager()

    def run(self):
        self.is_running = True
        self.particle_manager.add_particles()
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.dt = self.clock.tick(60) / 18

    def handle_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        self.particle_manager.update(self.dt)

    def draw(self):
        self.screen.fill("black")
        self.particle_manager.draw(self.screen)


if __name__ == "__main__":
    app = App()
    app.run()
