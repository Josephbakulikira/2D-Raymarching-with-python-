import pygame

class Boundary:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius

    def display(self, screen, color):
        pygame.draw.circle(screen, color, self.position, self.radius)
