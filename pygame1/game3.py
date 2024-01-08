import pygame
import random

#Inicialization
pygame.init()

#Screen
width = 1080
height = 640
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

#Basic settings
fps = 60
clock = pygame.time.Clock()
player_start_lives = 5
enemy_start_speed = 2
enemy_speed_acceleration = 0.5
score = 0

player_lives = player_start_lives
enemy_speed = enemy_start_speed

enemy_x = random.choice([-1,1])
enemy_y = random.choice([-1,1])

#Images
background_image = pygame.image.load("pyprogramovani/pygame1/img/background1.jpg")
background_image_rect = background_image.get_rect()
background_image_rect.topleft = (0,0)

enemy_image = pygame.image.load("pyprogramovani/pygame1/img/enemy1.png")
enemy_image_rect = enemy_image.get_rect()
enemy_image_rect.center = (width/2, height/2)

#Colours
black = (0,0,0)
white = (255,255,255)
yellow = (230, 230, 0)

#Fonts
custom_font_medium = pygame.font.Font("pyprogramovani/pygame1/fonts/font1/font1.ttf",32)
custom_font_medium_large = pygame.font.Font("pyprogramovani/pygame1/fonts/font1/font1.ttf",64)
custom_font_big = pygame.font.Font("pyprogramovani/pygame1/fonts/font1/font1.ttf",128)

#Texts
game_over_text = custom_font_big.render("GAME OVER",True,yellow)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (width//2, height//2-150)

#Sounds
success_click = pygame.mixer.Sound("pyprogramovani/pygame1/zvuk/success_click.mp3")
miss_click = pygame.mixer.Sound("pyprogramovani/pygame1/zvuk/miss_click.mp3")
pygame.mixer.music.load("pyprogramovani/pygame1/zvuk/arcade_music1.mp3")

success_click.set_volume(0.2)
miss_click.set_volume(0.2)
pygame.mixer.music.set_volume(0.1)

#Main cycle
running = True

pygame.mixer.music.play(-1,0.0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]

            #Enemy clicked?
            if enemy_image_rect.collidepoint(click_x, click_y):
                score+=1
                success_click.play()
                enemy_speed +=enemy_speed_acceleration

                enemy_x = random.choice([-1,1])
                enemy_y = random.choice([-1,1])

                previous_x = enemy_x
                previous_y = enemy_y
                while previous_x == enemy_x and previous_y == enemy_y:
                    enemy_x = random.choice([-1,1])
                    enemy_y = random.choice([-1,1])

            else:
                miss_click.play()
                player_lives -=1

    #Enemy movement
    enemy_image_rect.x += enemy_x * enemy_speed
    enemy_image_rect.y += enemy_y * enemy_speed

    if enemy_image_rect.left < 0 or enemy_image_rect.right >= width:
        enemy_x = -1 * enemy_x
    elif enemy_image_rect.top < 0 or enemy_image_rect.bottom >= height:
        enemy_y = -1 * enemy_y
     

    #Texts update
    score_text = custom_font_medium.render(f"SKORE {score}",True, yellow)
    score_text_rect = score_text.get_rect()
    score_text_rect.topright = (width -100,20)

    lives_text = custom_font_medium.render(f"HP {player_lives}",True, yellow)
    lives_text_rect = lives_text.get_rect()
    lives_text_rect.topleft = (100,20)
    #Images
    screen.blit(background_image, background_image_rect)
    screen.blit(enemy_image, enemy_image_rect)

    #Texts
    screen.blit(score_text, score_text_rect)
    screen.blit(lives_text, lives_text_rect)
    retry_text = custom_font_medium_large.render(f"SKORE {score}",True,yellow)
    retry_text_rect = retry_text.get_rect()
    retry_text_rect.center = (width//2, height//2)
    #Update screen
    pygame.display.update()

    #Slowing cycle
    clock.tick(fps)

    #End screen check
    if player_lives == 0:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(retry_text, retry_text_rect)
        pygame.display.update()

        pygame.mixer.music.stop()

        paused = True
        while paused:
            #Play again?
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = player_start_lives
                    enemy_speed = enemy_start_speed
                    enemy_image_rect.center = (width//2,height//2)
                    enemy_x = random.choice([-1,1])
                    enemy_y = random.choice([-1,1])
                    pygame.mixer.music.play(-1,0.0)
                    paused = False
                elif event.type == pygame.QUIT:
                    paused  =False
                    running = False
 #End
pygame.quit()