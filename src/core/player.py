import pygame
from src.core.bullet import Bullet
import src.core.filepath as filepath

class Player:
    def __init__(self, x, y, enemys):
        self.image = pygame.image.load(filepath.PLAYER_PATH)
        self.x = x
        self.y = y
        self.enemys = enemys
        self.x_change = 0
        self.score = 0
        self.bullets = []

    def move(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x = 0
        if self.x >= 736:
            self.x = 736
        for bullet in self.bullets:
            bullet.move()
            for enemy in self.enemys:
                if bullet.isCollide(enemy):
                    self.score += 1
                    print(self.score)
                    self.bullets.remove(bullet)
                    self.enemys.remove(enemy)
           
                
            

    def fire(self):
        bullet = Bullet(self.x, self.y)
        bullet.fire(self.x, self.y)
        self.bullets.append(bullet)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)
        self.bullets = [bullet for bullet in self.bullets if bullet.state == "fire"]
