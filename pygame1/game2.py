import pygame
import random

pygame.init()

# Získejte rozměry obrazovky
width = 1900
height = 1000

# Screen
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alien Invasion")

#Main settings
player_start_lives = 200
player_speed = 10
enemy_speed = 5
enemy_speed_acceleration = 0.5
enemy_behind_border = 20
score = 0

player_lives = player_start_lives
enemy_current_speed = enemy_speed

#FPS and clocks
fps = 60
clock = pygame.time.Clock() 

#Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Fonts
custom_font1 = pygame.font.Font("pygame1/fonts/font1/font1.ttf",50)
custom_font2 = pygame.font.Font("pygame1/fonts/font1/font1.ttf",64)
custom_font3 = pygame.font.Font("pygame1/fonts/font1/font1.ttf",164)
custom_font4 = pygame.font.Font("pygame1/fonts/font1/font1.ttf",84)

#TEXT
boss_name_text = custom_font2.render("BOSS",True , white)
boss_name_text_rect = boss_name_text.get_rect()
boss_name_text_rect.center = (width //1.9, height // 8)

hp_text = custom_font1.render(f"HP {player_lives}", True , white)
hp_text_rect = hp_text.get_rect()
hp_text_rect.center = (width //2, height // 1.1)

game_over_text = custom_font3.render(f"GAME OVER", True, white)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (width //2, height //4)

retry_text = custom_font4.render(f"RETRY", True, white)
retry_text_rect = retry_text.get_rect()
retry_text_rect.center = (width //2, height //2)

main_menu_text = custom_font4.render(f"MAIN MENU", True, white)
main_menu_text_rect = main_menu_text.get_rect()
main_menu_text_rect.center = (width //2, height //1.57)

exit_text = custom_font4.render(f"EXIT", True, white)
exit_text_rect = exit_text.get_rect()
exit_text_rect.center = (width //2, height //1.3)

#Sound
sound_hit = pygame.mixer.Sound("pygame1/zvuk/hit2.mp3")
sound_hit.set_volume(0.1)

sound_heart_beat = pygame.mixer.Sound("pygame1/zvuk/hearth_beat.mp3")
sound_heart_beat.set_volume(0.2)

pygame.mixer.music.load("pygame1/zvuk/arcade_music1.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.1)

draha_Y = [550, 650, 750]

#Images
player_image = pygame.image.load("pygame1/img/player.png")
player_image_rect = player_image.get_rect()
player_image_rect.center = (950,680)

enemy_image = pygame.image.load("pygame1/img/enemy1.png")
enemy0_image_rect = enemy_image.get_rect()
enemy0_image_rect.x = 600
enemy0_image_rect.centery = random.choice(draha_Y)

enemy1_image = pygame.image.load("pygame1/img/enemy1.png")
enemy1_image_rect = enemy1_image.get_rect()
enemy1_image_rect.x = 1350
enemy1_image_rect.centery = random.choice(draha_Y)

enemy2_image = pygame.image.load("pygame1/img/enemy4.png")
enemy2_image_rect = enemy2_image.get_rect()
enemy2_image_rect.x = 1350
enemy2_image_rect.centery = random.choice(draha_Y)

boss_enemy_angry_image = pygame.image.load("pygame1/img/boss_enemy_angry.png")
boss_enemy_angry_image_rect = boss_enemy_angry_image.get_rect()
boss_enemy_angry_image_rect.center = (1000,300)

#Main cycle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Keyboard movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_image_rect.top >500:
        player_image_rect.y -= player_speed
    elif  (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_image_rect.bottom <800:
        player_image_rect.y += player_speed

    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_image_rect.left >650:
        player_image_rect.x -= player_speed
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_image_rect.right <1350:
        player_image_rect.x += player_speed

    # Seznam výšek Y pro jednotlivé dráhy
    draha_Y = [550, 650, 750]

    # enemy0 movement
    if enemy0_image_rect.x > 1320:  # Pokud nepřítel překročí pravou hranici obrazovky
        enemy0_image_rect.x = 670   # Vrátíme ho z levé strany obrazovky
        enemy0_image_rect.centery = random.choice(draha_Y)  # Nastavíme novou náhodnou výšku Y na jednu z drah
    else:
        enemy0_image_rect.x += enemy_current_speed  # Jinak se nepřítel pohybuje dopředu

    #enemy1 movement
    if enemy1_image_rect.right < 670:  # Pokud druhý nepřítel překročí levou hranici obrazovky
        enemy1_image_rect.right = 1320   # Vrátíme ho z pravé strany obrazovky
        enemy1_image_rect.centery = random.choice(draha_Y)  # Nastavíme náhodnou výšku Y
    else:
        enemy1_image_rect.x -= enemy_current_speed  # Jinak se druhý nepřítel pohybuje zpět

    #enemy2 movement
    if enemy2_image_rect.right < 670:  # Pokud druhý nepřítel překročí levou hranici obrazovky
        enemy2_image_rect.right = 1320   # Vrátíme ho z pravé strany obrazovky
        enemy2_image_rect.centery = random.choice(draha_Y)  # Nastavíme náhodnou výšku Y
    else:
        enemy2_image_rect.x -= enemy_current_speed  # Jinak se druhý nepřítel pohybuje zpět

    #Collision check
    if player_image_rect.colliderect(enemy0_image_rect) or player_image_rect.colliderect(enemy1_image_rect) or player_image_rect.colliderect(enemy2_image_rect):
        player_lives -=1
        sound_hit.play()
        
    #Text
    hp_text = custom_font1.render(f"HP {player_lives}", True , white)
    hp_text_rect = hp_text.get_rect()
    hp_text_rect.center = (width //2, height // 1.1)

    #Znovu vykresleni obrazovky
    SCREEN.fill(black)

    #Sound
    if player_lives <50:
        sound_heart_beat.play()

    #GAMEOVER screen
    if player_lives == 0:
        sound_heart_beat.stop()
        SCREEN.blit(game_over_text, game_over_text_rect)
        SCREEN.blit(retry_text, retry_text_rect)
        pygame.draw.rect(SCREEN, red, (650, 450, 600, 100), 8)
        SCREEN.blit(main_menu_text, main_menu_text_rect)
        pygame.draw.rect(SCREEN, white, (650, 585, 600, 100), 8)
        SCREEN.blit(exit_text, exit_text_rect)
        pygame.draw.rect(SCREEN, white, (650, 720, 600, 100), 8)
            
        pygame.display.update()

        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    #ENTER = RETRY
                    if event.key == pygame.K_RETURN:
                            score = 0
                            player_lives = player_start_lives
                            enemy_current_speed = enemy_speed
                            player_image_rect.y = height//2
                            pause = False

                    #Změna barvy "tlacitek" podle pozice
                    if event.key == pygame.K_s:
                        pygame.draw.rect(SCREEN, white, (650, 450, 600, 100), 8)
                        pygame.draw.rect(SCREEN, red, (650, 585, 600, 100), 8)
                        pygame.display.update()
                            
                    if event.key == pygame.K_w:
                        pygame.draw.rect(SCREEN, red, (650, 450, 600, 100), 8)
                        pygame.draw.rect(SCREEN, white, (650, 585, 600, 100), 8)
                        pygame.display.update()

                    if event.type == pygame.QUIT:
                        pause = False
                        running = False

    #Tvary
    pygame.draw.rect(SCREEN,white,(650,500,700,300),8)
    
    pygame.draw.line(SCREEN, red, (658, 550), (1342,550), 4)
    pygame.draw.line(SCREEN, red, (658, 650), (1342,650), 4)
    pygame.draw.line(SCREEN, red, (658, 750), (1342,750), 4)    

    #Texts
    SCREEN.blit(hp_text,hp_text_rect)
    SCREEN.blit(boss_name_text,boss_name_text_rect)
    #Images blitting
    SCREEN.blit(player_image,player_image_rect)
    SCREEN.blit(enemy_image,enemy0_image_rect)
    SCREEN.blit(enemy1_image,enemy1_image_rect)
    SCREEN.blit(enemy2_image,enemy2_image_rect)
    SCREEN.blit(boss_enemy_angry_image,boss_enemy_angry_image_rect)
    
    #Screen update
    pygame.display.update()

    #Clock tick
    clock.tick(fps)

#End
pygame.quit() 
