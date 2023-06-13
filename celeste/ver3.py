import pygame
import random

SCREEN_SIZE = (800, 600)
PARTICLE_COUNT = 100


class Particle:
    def __init__(self, pos, radius, speed) -> None:
        self.pos = pos
        self.radius = radius
        self.speed = speed


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.is_running = None
        self.particles = []

    def run(self):
        self.is_running = True
        self.add_particles()
        while self.is_running:
            self.input()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60)

    def add_particles(self):
        for _ in range(PARTICLE_COUNT):
            particle = Particle(
                [
                    random.randint(-100, SCREEN_SIZE[0] + 100),
                    random.randint(-100, SCREEN_SIZE[1] + 100),
                ],
                random.randint(3, 6),
                random.randint(4, 8),
            )
            self.particles.append(particle)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

    def update(self):
        for particle in self.particles:
            particle.pos[0] -= particle.speed
            if particle.pos[0] < -100:
                particle.pos[0] = SCREEN_SIZE[0] + 100

    def draw(self):
        self.screen.fill("black")

        for particle in self.particles:
            pygame.draw.circle(self.screen, "white", particle.pos, particle.radius)

        pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.run()
