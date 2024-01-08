import pygame
import random


# Inicializace
pygame.init()
#barvy
black = (0,0,0)
# Obrazovka
sirka = 1080
vyska = 640
screen = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("Hovnožrout")

#Základní nastavení
distance = 10
fps = 60
clock = pygame.time.Clock()
skore = 0
zivoty = 3


# Barva pozadí
barva_pozadi = (192, 192, 192)
screen.fill(barva_pozadi)

# Obrázek "postava"
postava_image = pygame.image.load("pyprogramovani/pygame1/img/postava.png")
postava_rect = postava_image.get_rect()
postava_rect.center = (sirka // 2.5, vyska // 2.5)


# Obrázek "poop"
poop_image = pygame.image.load("pyprogramovani/pygame1/img/poop.png")
poop_rect = poop_image.get_rect()
poop_rect.center = (sirka // 2, vyska // 2.5)

#nastavení systémového fontu
system_font = pygame.font.SysFont("calibri", 64)
custom_font = pygame.font.Font("pyprogramovani/pygame1/fonts/font1/font1.ttf",32)
custom_font2 = pygame.font.Font("pyprogramovani/pygame1/fonts/font1/font1.ttf",20)

#Font a text ale custom

#Text1
custom_text =custom_font.render("HHHHHOOOOVNOOOZROUUT",True, black)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (540, 25)

#Zvuky
sound_boom = pygame.mixer.Sound("pyprogramovani/pygame1/zvuk/boom.wav")

#Hudba v pozadí  
pygame.mixer.music.load("pyprogramovani/pygame1/zvuk/lacrimosa.mp3")
pygame.mixer.music.play(-1,0.0)

#Zmena Hlasitosti
sound_boom.set_volume(0.4)

#Přehrání zvuku
sound_boom.play()

# Hlavní herní smyčka
pokracovat = True

while pokracovat:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovat = False
    
    #Pohyb pomocí klávesnice
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and postava_rect.top >60:
        postava_rect.y -=distance
    elif (keys[pygame.K_DOWN]or  keys[pygame.K_s]) and postava_rect.bottom < vyska:
        postava_rect.y +=distance
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a])and postava_rect.left >0:
        postava_rect.x -=distance
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d])and postava_rect.right <sirka:
        postava_rect.x +=distance
    
    #Pohyb nepritele
    

    #Pohyb pomocí myši
    if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
        postava_rect.centerx = event.pos[0]
        postava_rect.centery = event.pos[1]
    
    #Aby po pohybu nezustal obrazek
    screen.fill(barva_pozadi)
    #tvary
    pygame.draw.line(screen, black, (0,50),(sirka,50), 2)
    #Kolize - řešení
    
    if postava_rect.colliderect(poop_rect):
        poop_rect.centerx =random.randint(0+32,sirka)
        poop_rect.centery = random.randint(60,vyska)
        sound_boom.play()
        skore +=1

    #Text skore
    custom_text2 =custom_font2.render(f"SKORE {skore} ",True, black)
    custom_text_rect2 = custom_text2.get_rect()
    custom_text_rect2.center = (130, 25)

    #Text zivoty
    custom_text3 = custom_font2.render(f"ZIVOTY  {zivoty}",True, black)
    custom_text_rect3 = custom_text3.get_rect()
    custom_text_rect3.center = (950,25)

    # Přidání obrázků na obrazovku
    screen.blit(postava_image, postava_rect)
    screen.blit(poop_image, poop_rect)
    screen.blit(custom_text,custom_text_rect)
    screen.blit(custom_text2,custom_text_rect2)
    screen.blit(custom_text3,custom_text_rect3)

    # Aktualizace obrazovky
    pygame.display.update()

    #Tikání hodin
    clock.tick(fps)

# Konec
pygame.quit()
