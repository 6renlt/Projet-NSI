# Ceci est le fichier principal
import pygame
from pygame.locals import *
pygame.init()

largeur=800
longueur=800

def jeu_beret():
    screen = display.set_mode((largeur,longueur))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit ()

                
                
            
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
    

def temps():
    
     
def objet():

    
def fin() :
    screen = pygame.display.set_mode((800, 800))
    police = pygame.font.SysFont("ubuntu",100)
    image_texte = police.render("FIN",1,(255,255,255))
    screen.blit(image_texte, (300,350))
    pygame.display.flip()
    
    
    
    
