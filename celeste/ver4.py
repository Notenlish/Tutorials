import pygame
import random
import math

SCREEN_SIZE = (800, 450)  # make sure to keep the 16:9 ratio
PARTICLE_COUNT = 100


class Particle:
    def __init__(self, pos, radius, speed, time_offset, wave_speed) -> None:
        self.pos = pos
        self.radius = radius
        self.speed = speed
        self.time_offset = time_offset
        self.wave_speed = wave_speed


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.is_running = None
        self.particles = []
        self.time = 0
        self.background = pygame.image.load("tutorial/background.png").convert()
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)

    def run(self):
        self.is_running = True
        self.add_particles()
        while self.is_running:
            pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")
            self.input()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60)
            self.time += self.dt / 1000

    def add_particles(self):
        for _ in range(PARTICLE_COUNT):
            particle = Particle(pos = [
                                    random.randint(-100, SCREEN_SIZE[0] + 100),
                                    random.randint(-100, SCREEN_SIZE[1] + 100)
                                ],
                                radius = random.randint(2, 4),
                                speed = random.randint(6, 12),
                                time_offset = random.randint(-4, 3),
                                wave_speed = 1 + (random.randint(-15, 15) / 10))
            self.particles.append(particle)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

    def update(self):
        for particle in self.particles:
            # make the particle go left
            particle.pos[0] -= particle.speed

            if particle.pos[0] < -100:  # particle is out of screen
                particle.pos[0] = SCREEN_SIZE[0] + 100

                # if the particle is also too up or down 
                if particle.pos[1] < -100 or particle.pos[1] > SCREEN_SIZE[1] + 100:
                    particle.pos[1] = random.randint(100, SCREEN_SIZE[1] - 100)
            
            # change the y value
            particle.pos[1] += math.sin((self.time + particle.time_offset)) * particle.wave_speed
    
    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.background, (0, 0))

        for particle in self.particles:
            pygame.draw.circle(self.screen, "white", particle.pos, particle.radius)
        
        pygame.display.update()


if __name__ == '__main__':
    app = App()
    app.run()