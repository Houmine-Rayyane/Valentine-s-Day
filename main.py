import random
import pygame
from pygame import mixer
from sys import exit
import random 


pygame.init()
mixer.init()

mixer.music.load('audio/Closer.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()

FPS = 60
Width, Height = 600,400
Win = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Valentine')

teddy_bear = pygame.image.load('Pics/teddy bear.png')
bear_surf = teddy_bear.get_rect(midbottom=(300,275))

rose = pygame.image.load('Pics/rose.gif')
rose_resized = pygame.transform.scale(rose,(300,400))
rose_rotated = pygame.transform.rotate(rose_resized,90)
rose_surf = rose_rotated.get_rect(midbottom=(280,350))


txt_font = pygame.font.Font('font/gamefont.ttf',20)
txt_surf = txt_font.render('Would you be my Valentine ?', False, 'Dark red').convert()

txt3_font = pygame.font.Font('font/gamefont.ttf',10)
txt3_surf = txt3_font.render("It's been a great pleasure being your man,and I cherish",False,'Dark red').convert()
txt4_surf = txt3_font.render('every moment that we get to spend time with each other',False,'Dark red').convert()

txt2_font = pygame.font.Font('font/gamefont.ttf',15)
txt2_surf = txt2_font.render('Click on your answer', False, 'Dark red').convert()

yesno_font = pygame.font.Font('font/gamefont.ttf',15)

yesno_surf1 = yesno_font.render('Yes', False, 'Dark red').convert()
yes_rect = yesno_surf1.get_rect(midbottom =(80,330))

yesno_surf2 = yesno_font.render('No', False, 'Dark red').convert()
no_rect = yesno_surf2.get_rect(midbottom =(500,330))

Continue = True 

clk = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if Continue:
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_y:
                   #Continue = False
                #if event.key == pygame.K_n:
                    #no_rect.left = random.randint(1,500) 
                    #no_rect.bottom = random.randint(300,400)
            if event.type ==pygame.MOUSEMOTION:
                if no_rect.collidepoint(event.pos):
                    no_rect.left = random.randint(1,500) 
                    no_rect.bottom = random.randint(300,400)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    
                    Continue = False

    if Continue:
        Win.fill('pink')
        Win.blit(teddy_bear,bear_surf)
        Win.blit(txt_surf,(45,60))
        Win.blit(txt2_surf,(150,250))
        Win.blit(yesno_surf1,yes_rect)
        Win.blit(yesno_surf2,no_rect)
        
    else:
        Win.fill('pink')
        Win.blit(rose_rotated,rose_surf)
        Win.blit(txt3_surf,(15,70))
        Win.blit(txt4_surf,(20,300))
        
        
        
        

    pygame.display.update()
    clk.tick(FPS)