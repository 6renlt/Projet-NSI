# Ceci est le fichier principal
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
current_time = 0

largeur=800
longueur=800


pygame.mixer.music.load('')
pygame.mixer.music.play()
Sound.play(loops=1, maxtime=0, fade_ms=0)

def jeu_beret():
    screen = display.set_mode((largeur,longueur))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit ()
                
        pygame.display.flip()
        clock.tick(60)
        current_time = pygame.time.get_ticks()
    
    
                

    
def map():


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
    

def timmer():
def timer(time_start, t):
    print((time()-time_start))
    return ((time()-time_start)>=t)

def objet():
    
    
def fin() :
    screen = pygame.display.set_mode((largeur, longueur))
    police = pygame.font.SysFont("ubuntu",100)
    image_texte = police.render("FIN",1,(255,255,255))
    screen.blit(image_texte, (300,350))
    pygame.display.flip()
    
    
    
    
