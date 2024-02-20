import pygame
import random


# Inicializace
pygame.init()
#barvy
black = (0,0,0)

# Screen
width = 1080
height = 640
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

#Main settings
distance = 10
fps = 60
clock = pygame.time.Clock()
score = 0
hp = 3


# Background colour
background_color = (192, 192, 192)
SCREEN.fill(background_color)

# Image: "player"
player_image = pygame.image.load("pygame1/img/postava.png")
player_rect = player_image.get_rect()
player_rect.center = (width // 2.5, height // 2.5)


# Image: "poop"
poop_image = pygame.image.load("pygame1/img/poop.png")
poop_rect = poop_image.get_rect()
poop_rect.center = (width // 2, height // 2.5)

#Font settings
system_font = pygame.font.SysFont("calibri", 64)
custom_font = pygame.font.Font("pygame1/fonts/font1/font1.ttf",32)
custom_font2 = pygame.font.Font("pygame1/fonts/font1/font1.ttf",20)

#Text1
custom_text =custom_font.render("PACMAN",True, black)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (540, 25)

#Sounds
sound_boom = pygame.mixer.Sound("pygame1/zvuk/boom.wav")

#Background music
pygame.mixer.music.load("pygame1/zvuk/lacrimosa.mp3")
pygame.mixer.music.play(-1,0.0)

#Change volume
sound_boom.set_volume(0.4)

#Volume play
sound_boom.play()

# Main cycle
pokracovat = True

while pokracovat:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovat = False
    
    #Keyboard movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_rect.top >60:
        player_rect.y -=distance
    elif (keys[pygame.K_DOWN]or  keys[pygame.K_s]) and player_rect.bottom < height:
        player_rect.y +=distance
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a])and player_rect.left >0:
        player_rect.x -=distance
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d])and player_rect.right <width:
        player_rect.x +=distance
    
    #Mouse movement
    if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
        player_rect.centerx = event.pos[0]
        player_rect.centery = event.pos[1]
    
    #Aby po pohybu nezustal obrazek
    SCREEN.fill(background_color)

    #tvary
    pygame.draw.line(SCREEN, black, (0,50),(width,50), 2)

    #Collision
    if player_rect.colliderect(poop_rect):
        poop_rect.centerx =random.randint(0+32,width)
        poop_rect.centery = random.randint(60,height)
        sound_boom.play()
        score +=1

    #Text score
    custom_text2 =custom_font2.render(f"SCORE {score} ",True, black)
    custom_text_rect2 = custom_text2.get_rect()
    custom_text_rect2.center = (130, 25)

    #Text lives
    custom_text3 = custom_font2.render(f"LIVES  {hp}",True, black)
    custom_text_rect3 = custom_text3.get_rect()
    custom_text_rect3.center = (950,25)

    # Images display blitting
    SCREEN.blit(player_image, player_rect)
    SCREEN.blit(poop_image, poop_rect)
    SCREEN.blit(custom_text,custom_text_rect)
    SCREEN.blit(custom_text2,custom_text_rect2)
    SCREEN.blit(custom_text3,custom_text_rect3)

    # Screen update
    pygame.display.update()

    # Clock ticks
    clock.tick(fps)

# End
pygame.quit()
