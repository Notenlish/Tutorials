import pygame

SCREEN_SIZE = (800, 600)



class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.is_running = None

    def run(self):
        self.is_running = True
        while self.is_running:
            self.input()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

    def update(self):
        pass
    
    def draw(self):
        self.screen.fill("black")
        pygame.display.update()


if __name__ == '__main__':
    app = App()
    app.run()