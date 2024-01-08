import pygame
import random

#Inicialization
pygame.init()

#Screen
width = 1080
height = 640
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

#Basic Settings
fps =60
clock = pygame.time.Clock()

#Classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x ,y ):
        super().__init__()
        self.image = pygame.image.load("pygame1/img/enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.speed = random.randint(1,6)

    def update(self):
        self.move()

    def move(self):
        self.rect.y += self.speed

#Create group of enemies
enemy_group = pygame.sprite.Group()
for i in range(10):
    one_enemy = Enemy(i*70,50)
    enemy_group.add(one_enemy)

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("pygame1/img/player.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = random.randint(1,6)

    def update(self):
        self.move()

    def move(self):
        self.rect.y -= self.speed
    
#Create group of players
player_group = pygame.sprite.Group()
for i in range(10):
    one_player = Player(i*70,height-50)
    player_group.add(one_player)
#Fonts

#Text

#Images

#Sound


#Main Cycle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Screen fill black
    screen.fill((0,0,0))
    #Update group of enemies
    enemy_group.update()
    enemy_group.draw(screen)

    #Update group of players
    player_group.update()
    player_group.draw(screen)

    #Update screen
    pygame.display.update()

    #Slow cycle
    clock.tick(fps)


#End
pygame.quit()