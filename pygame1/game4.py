import pygame
import random

#Inicialization
pygame.init()

#Screen
width = 1800  #X
height = 900  #Y
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

#Basic Settings
fps =60
clock = pygame.time.Clock()

#Classes
class Game:
    def __init__(self,our_player, group_of_enemies):
        self.score = 0 
        self.round_number = 0

        self.round_time = 0
        self.slow_down_cycle = 0

        self.our_player = our_player
        self.group_of_enemies = group_of_enemies

        #Music in background
        pygame.mixer.music.load("pygame1/zvuk/arcade_music1.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.1)

        #Font
        self.custom_font_small = pygame.font.Font("pygame1/fonts/font1/font1.ttf",24)
        self.custom_font_medium = pygame.font.Font("pygame1/fonts/font1/font1.ttf",64)
        self.custom_font_large = pygame.font.Font("pygame1/fonts/font1/font1.ttf",128)
    
    #Update game
    def update(self):
        #Time
        self.slow_down_cycle +=1 
        if self.slow_down_cycle == fps:
            self.round_time += 1
            self.slow_down_cycle = 0
            print(self.round_time)
    
    #Collision check
    
    
    #Drawing images
    def draw(self):
        
        #Colours
        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)

        #Text
         
        hp_text = self.custom_font_small.render(f"HP {self.our_player.hp}", True, white)
        hp_text_rect = hp_text.get_rect()
        hp_text_rect.centerx = width // 2
        hp_text_rect.centery = height // 1.1

        score_text= self.custom_font_small.render(f"SKORE {self.score}", True, white)
        score_text_rect = score_text.get_rect()
        score_text_rect.centerx = width // 1.1
        score_text_rect.centery = height // 5

        round_text = self.custom_font_small.render(f"ROUND {self.round_number}", True, white)
        round_text_rect = round_text.get_rect()
        round_text_rect.centerx = width // 1.1
        round_text_rect.centery = height // 7

        time_text = self.custom_font_small.render(f"TIME {self.round_time}", True, white)
        time_text_rect = time_text.get_rect()
        time_text_rect.centerx = width // 1.1
        time_text_rect.centery = height // 4

        #Blitting
        screen.blit(hp_text,hp_text_rect)
        screen.blit(score_text,score_text_rect)
        screen.blit(round_text,round_text_rect)
        screen.blit(time_text,time_text_rect)

        #Objects
        pygame.draw.rect(screen, white,(width // 3, height // 2,width //3, height //3),10)
    
    #Collision detection
    def check_collision(self):
        collided_enemy = pygame.sprite.spritecollideany(self.our_player, self.group_of_enemies)

        
            
    def start_new_level(self):
        pass

    #pause game
    def pause_game(self):
        pass
    
    #Exit game
    def exit_game(self):
        pass
    
    #Restart game
    def restart_game(self):
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame1/img/player.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = width//2  #Player spawn position X
        self.rect.centery = height //1.5 #Player spawn position Y

        self.hp = 3
        self.speed = 5
       

        self.collision_sound = pygame.mixer.Sound("pygame1/zvuk/hit2.mp3")
        self.collision_sound.set_volume(0.2)

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > width//3:  # Až budu dělat white rectangle tak přepíšu hodnoty
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < width//1.5:
            self.rect.x += self.speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top > height//2:  # Až budu dělat white rectangle tak přepíšu hodnoty
            self.rect.y -= self.speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom < height//1.2:
            self.rect.y += self.speed

    def reset(self):
        pass

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, enemy_type):
        super().__init__()
        
        #Image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (width//2,height//1.5) # enemy spawn position

        #types of enemy
        self.enemy_type = enemy_type

        #Set enemy movement
        self.x = random.choice([-1, 1])
        self.y = random.choice([-1, 1])
        self.speed = random.randint(1,5)

    def update(self):
        #Enemy movement
        self.rect.x += self.x * self.speed
        self.rect.y += self.y * self.speed	

        #Reflection
        if self.rect.left <width//3 or self.rect.right > width //1.5 :   # Až budu dělat white rectangle tak přepíšu hodnoty  X 
            self.x = -1 * self.x
        elif self.rect.top < height//2 or self.rect.bottom > height //1.2:  # Až budu dělat white rectangle tak přepíšu hodnoty  Y
            self.y = -1 * self.y


# ============ USING LOGIC ===============
#Group of enemies
enemy_group = pygame.sprite.Group()

#Testing
one_enemy = Enemy(500,500 ,pygame.image.load("pygame1/img/enemy1.png"),0)
enemy_group.add(one_enemy)
one_enemy = Enemy(500,500 ,pygame.image.load("pygame1/img/enemy2.png"),1)
enemy_group.add(one_enemy)
one_enemy = Enemy(500,500 ,pygame.image.load("pygame1/img/enemy3.png"),2)
enemy_group.add(one_enemy)
one_enemy = Enemy(500,500 ,pygame.image.load("pygame1/img/enemy4.png"),3)
enemy_group.add(one_enemy)

#Group of players
player_group = pygame.sprite.Group()
one_player = Player()
player_group.add(one_player)

#Object game
my_game = Game(one_player,enemy_group)

# ================ LOGIC =============
#Main Cycle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Screen fill
    screen.fill((0, 0, 0))
    
    #Group of enemies update
    enemy_group.draw(screen)
    enemy_group.update()

    #Group of playrs update
    player_group.draw(screen)
    player_group.update()

    #Object update
    my_game.update()
    my_game.draw()

    #Update screen
    pygame.display.update()

    #Slow cycle
    clock.tick(fps)


#End
pygame.quit()