# Upgrade CPU

import pygame
import pyganim
from .stage import Stage, Text


class Stage18(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.bg = pygame.image.load("images/CPU Upgrade.png").convert()

        self.reset()
        
    def reset(self):
        self.texts = []
        self.objects = []
        self.total = 0
        self.current_selected = [0, 0, 2]
        self.current_row = 0

    def update(self, input, tick):
        self.texts = [Text("Upgrade your computer to minimize lag", (0, 0, 0), self._center_text)]

        if input.up:
            self.current_selected[self.current_row] -= 1
            self.current_selected[self.current_row] = max(0, self.current_selected[self.current_row])
        if input.down:
            self.current_selected[self.current_row] += 1
            self.current_selected[self.current_row] = min(2, self.current_selected[self.current_row])
        if input.left:
            self.current_row -= 1
            self.current_row = max(0, self.current_row)
        if input.right:
            self.current_row += 1
            self.current_row = min(2, self.current_row)

        if self.current_selected == [2, 2, 1]:
            return True

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        super().draw(screen)
        
        color = (0, 255, 0)
        for i, (x, y) in enumerate([(50, 420), (340, 440), (600, 420)]):
            rect = pygame.Rect(x, y + (self.current_selected[i] * 38), 150, 40)
            pygame.draw.rect(screen, color, rect, 1)

        self._iterate_all(self.objects, "draw", {"screen": screen})