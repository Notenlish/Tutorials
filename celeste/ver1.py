import pygame

SCREEN_SIZE = (800, 600)


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.is_running = False
        self.dt = 0
        self.events = []

    def run(self):
        self.is_running = True
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.dt = self.clock.tick(60)

    def handle_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill("black")


if __name__ == "__main__":
    app = App()
    app.run()
