import pygame
import src.core.filepath as filepath
from src.core.player import Player
from src.core.enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Game")
        
        
        self.icon = pygame.image.load(filepath.ICON_PATH)
        self.bg = pygame.image.load(filepath.BACKGROUND_PATH)
        self.bg = pygame.transform.scale(self.bg, (800, 600))
        pygame.display.set_icon(self.icon)
        
        self.bg_color = (85, 92, 92)
        self.running = True
        
        self.enemys = []
        for i in range(6):
            self.enemys.append(Enemy())
        
        self.player = Player(x=370, y=480,enemys=self.enemys)
        
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.x_change = -0.3
                elif event.key == pygame.K_RIGHT:
                    self.player.x_change = 0.3
                elif event.key == pygame.K_SPACE:
                    self.player.fire() 
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.player.x_change = 0

    def update(self):
        self.player.move()
        for enemy in self.enemys:
            enemy.move()    
        

    def draw(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.bg, (0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemys:
            enemy.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
