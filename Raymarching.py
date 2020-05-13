import pygame
import os
from Boundary import Boundary
from ray import Ray
from random import randint

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
size = (width, height)
#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)

#pygame configurations
pygame.init()
pygame.display.set_caption("2D Raymarching")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
screen_offset = 50



object_count = 10
angle = 0
objects = []

for i in range(object_count):
    obj = Boundary(randint(screen_offset, width - screen_offset), randint(screen_offset, height - screen_offset), randint(20, 100))
    objects.append(obj)


run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ray = Ray(width//2, height//2, 0, screen, white)
    ray.angle = angle

    screen.fill(black)
    for object in objects:
        object.display(screen, white)

    ray.March(objects)

    for pt in ray.collisions:
        pygame.draw.circle(screen, white, (int(pt[0]), int(pt[1])), 1)

    angle += 0.005

pygame.quit()
