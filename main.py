# Ceci est le fichier principal
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
current_time = 0

longueur=800
hauteur=465




def jeu_beret():
    ecran = pygame.display.set_mode((longueur, hauteur))
    image1 = pygame.image.load("map easy 1.jpg").convert_alpha()
    ecran.blit(image1, (0,0))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit ()
            if event.type == pygame.KEYDOWN:
                continuer = False
        pygame.display.flip()

def personnages():
    personnage_test = pygame.Rect((360,240), (32,32))
    pygame.key.set_repeat(1,20)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    personnage_test.move_ip((5,0))
                elif event.key == pygame.K_UP:
                    personnage_test.move_ip((0,-5))
                elif event.key == pygame.K_LEFT:
                    personnage_test.move_ip((-5,0))
                elif event.key == pygame.K_DOWN:
                    personnage_test.move_ip((0,5))
    

def temps(): 
    chrono = False
    start_ticks=pygame.time.get_ticks()#lance le chrono
    while not chrono :
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds<10:
            print(seconds)
        else :
            chrono = True
            fin()
            
 

def musique():
    pygame.mixer.music.load('')
    pygame.mixer.music.play()
    Sound.play(loops=1, maxtime=0, fade_ms=0)


def objet():
    
    
def fin() :
    screen = pygame.display.set_mode((longueur, hauteur))
    image2 = pygame.image.load('game_over.jpeg')
    image2 = image.convert()
    screen. blit(image, (82,50))
    pygame.display.flip()
    
    
    
