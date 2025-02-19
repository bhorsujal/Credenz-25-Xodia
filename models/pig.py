import pygame
import random

pig_img = pygame.image.load("ui/images/pig.png")

# JUST FOR REFERENCE. DO NOT MAKE ANY CHANGES IN THIS.


class Pig:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pig_img, (40, 40))
        self.x, self.y = x, y
        self.rect = self.image.get_rect()

    def draw(self, screen):
        self.rect.center = (int(self.x), int(self.y))
        screen.blit(self.image, self.rect)

    def reset(self, min_x=500, max_x=700):
        self.x = random.randint(min_x, max_x)
        self.y = random.randint(280, 380)
