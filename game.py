import pygame
import random
from config import *

class Game:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.map = map
        self.map_pos = (50, 100)
        self.font = pygame.font.SysFont("Arial", 36)

        self.score = 0

    def create(self):
        pygame.draw.rect(self.surface, (207, 192, 181), (self.map_pos[0], self.map_pos[1], 400, 400))
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.surface, (200, 173, 160), (self.map_pos[0] + i * 100, self.map_pos[1] + j * 100, 100, 100), 5)
                if self.map[i][j] != "":
                    color = self.get_color(i, j)

                    text = self.font.render(str(self.map[i][j]), True, (119, 110, 101))
                    pygame.draw.rect(self.surface, color, (self.map_pos[0] + i * 100 + 5, self.map_pos[1] + j * 100 + 5, 90, 90))
                    self.surface.blit(text, (self.map_pos[0] + i * 100 + 50 - text.get_width() // 2, self.map_pos[1] + j * 100 + 50 - text.get_height() // 2))

    def interface(self):
        pygame.draw.rect(self.surface, (250, 250, 239), (0, 0, 800, 100))
        self.score_text = self.font.render(f"Score: {self.score}", True, (119, 110, 101))
        self.surface.blit(self.score_text, (50, 25))

    def update(self, dt):
        self.surface.fill((250, 250, 239))
        self.create()
        self.interface()

        pygame.display.flip()

    def get_color(self, i, j):
        if self.map[i][j] == "2":
            color = (239, 228, 219)
        elif self.map[i][j] == "4":
            color = (236, 224, 200)
        elif self.map[i][j] == "8":
            color = (242, 177, 121)
        elif self.map[i][j] == "16":
            color = (245, 149, 99)
        elif self.map[i][j] == "32":
            color = (246, 124, 95)
        elif self.map[i][j] == "64":
            color = (246, 94, 59)
        elif self.map[i][j] == "128":
            color = (237, 207, 114)
        elif self.map[i][j] == "256":
            color = (237, 204, 97)
        elif self.map[i][j] == "512":
            color = (237, 200, 80)
        elif self.map[i][j] == "1024":
            color = (237, 197, 63)
        elif self.map[i][j] == "2048":
            color = (237, 194, 46)
        return color

    def add_new(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.map[i][j] == "":
                    empty.append((i, j))
        if len(empty) > 0:
            pos = random.choice(empty)
            self.map[pos[0]][pos[1]] = "2"

    def move(self, direction):
        if direction == "left":
            for j in range(4):
                for i in range(1, 4):  # Починаємо перевірку з другого рядка
                    if self.map[i][j] != "":
                        for k in range(i, 0, -1):  # Перевіряємо всі рядки вище поточного
                            if self.map[k - 1][j] == "":
                                self.map[k - 1][j] = self.map[k][j]
                                self.map[k][j] = ""
                            elif self.map[k - 1][j] == self.map[k][j]:
                                self.map[k - 1][j] = str(int(self.map[k - 1][j]) * 2)
                                self.map[k][j] = ""
                                self.score += int(self.map[k - 1][j])
        elif direction == "right":
            for i in range(4):
                for j in range(4):
                    if self.map[i][j] != "":
                        if i < 3:
                            if self.map[i + 1][j] == "":
                                self.map[i + 1][j] = self.map[i][j]
                                self.map[i][j] = ""
                            elif self.map[i + 1][j] == self.map[i][j]:
                                self.map[i + 1][j] = str(int(self.map[i + 1][j]) * 2)
                                self.map[i][j] = ""
                                self.score += int(self.map[i + 1][j])
        elif direction == "up":
            for i in range(4):
                for j in range(1, 4):  # Починаємо перевірку з другого стовпця
                    if self.map[i][j] != "":
                        for k in range(j, 0, -1):  # Перевіряємо всі стовпці лівіше поточного
                            if self.map[i][k - 1] == "":
                                self.map[i][k - 1] = self.map[i][k]
                                self.map[i][k] = ""
                            elif self.map[i][k - 1] == self.map[i][k]:
                                self.map[i][k - 1] = str(int(self.map[i][k - 1]) * 2)
                                self.map[i][k] = ""
                                self.score += int(self.map[i][k - 1])
        elif direction == "down":
            for i in range(4):
                for j in range(4):
                    if self.map[i][j] != "":
                        if j < 3:
                            if self.map[i][j + 1] == "":
                                self.map[i][j + 1] = self.map[i][j]
                                self.map[i][j] = ""
                            elif self.map[i][j + 1] == self.map[i][j]:
                                self.map[i][j + 1] = str(int(self.map[i][j + 1]) * 2)
                                self.map[i][j] = ""
                                self.score += int(self.map[i][j + 1])

        self.add_new()