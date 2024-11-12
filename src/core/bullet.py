import pygame
import src.core.filepath as filepath

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load(filepath.BULLET_PATH)
        self.x = x
        self.y = y
        self.state = "ready" 
        self.speed = 1  

    def fire(self, x, y):
        self.x = x
        self.y = y
        self.state = "fire"

    def move(self):
        if self.state == "fire":
            self.y -= self.speed
            if self.y <= 0:
                self.state = "ready"
                
    def isCollide(self, enemy):
        if self.state == "fire":
           distance = ((self.x - enemy.x)**2 + (self.y - enemy.y)**2)**0.5
           return distance < 27

    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self.image, (self.x + 20, self.y + 5))
