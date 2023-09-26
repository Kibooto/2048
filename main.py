import pygame

from game import Game

pygame.init()
pygame.font.init()

surface = pygame.display.set_mode((500, 600))
pygame.display.set_caption('2048 Game')

class Main:
    def __init__(self) -> None:
        self.playing = True
        self.clock = pygame.time.Clock()

        self.game = Game(surface)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.move("up")
                elif event.key == pygame.K_DOWN:
                    self.game.move("down")
                elif event.key == pygame.K_LEFT:
                    self.game.move("left")
                elif event.key == pygame.K_RIGHT:
                    self.game.move("right")

    def update(self):
        dt = self.clock.tick(60) / 1000
        self.game.update(dt)
        pygame.display.flip()

    def main(self):
        while self.playing:
            self.events()
            self.update()

if __name__ == '__main__':
    Main().main()
