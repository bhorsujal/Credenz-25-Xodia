import pygame
import random
import numpy as np


bird_img = pygame.image.load("ui/images/bird.png")

# JUST FOR REFERENCE. DO NOT MAKE ANY CHANGES IN THIS.

class Bird:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(bird_img, (40, 40))
        self.x, self.y = x, y
        self.initial_pos = (x, y)
        self.velocity = [0, 0]
        self.launched = False
        self.trajectory = []
        self.rect = self.image.get_rect()
        self.start_distance = None
        self.max_height = y
        self.launch_angle = 0

    def reset(self):
        self.x, self.y = self.initial_pos
        self.velocity = [0, 0]
        self.launched = False
        self.trajectory = []
        self.start_distance = None
        self.max_height = self.y
        self.launch_angle = 0

    def draw(self, screen):
        self.rect.center = (int(self.x), int(self.y))
        screen.blit(self.image, self.rect)
        if len(self.trajectory) > 1:
            pygame.draw.lines(screen, (255, 0, 0), False, [(int(x), int(y)) for x, y in self.trajectory], 2)

    def launch(self, power_x, power_y):
        if not self.launched:

            power_x += random.uniform(-0.5, 0.5)
            power_y += random.uniform(-0.5, 0.5)

            self.velocity = [power_x * 4, -power_y * 3.5]
            self.launched = True
            self.trajectory = [(self.x, self.y)]

            self.launch_angle = np.arctan2(-self.velocity[1], self.velocity[0])

    def update(self):
        if self.launched:
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.velocity[1] += 0.4

            self.max_height = min(self.max_height, self.y)

            self.velocity[0] += random.uniform(-0.1, 0.1)

            self.trajectory.append((self.x, self.y))

