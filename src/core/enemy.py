import random
import pygame
import src.core.filepath as filepath

class Enemy:
    def __init__(self):
       
        self.image = pygame.image.load(filepath.ENEMY_PATH)
        self.image = pygame.transform.rotate(self.image, 180)
        self.x = random.randint(40, 520)
        self.y = 10
        self.x_change = 0.3
        self.x_speed = (random.randint(2, 5) / 10)
        self.y_speed = random.randint(1, 3)
        

    def move(self):
        self.x += self.x_change
        if self.x <= random.randint(0, 30):
           self.x_change = self.x_speed
           self.y += self.y_speed
        if self.x >= random.randint(560, 736):
           self.x_change = self.x_speed * -1
           self.y += self.y_speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
