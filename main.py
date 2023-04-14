# Ceci est le fichier principal
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

current_time = 0

longueur=800
hauteur=465


perso = pygame.image.load("Fred.png")
perso = pygame.transform.scale(perso, (20,20))

def jeu_beret():                                                                     
        
    screen = pygame.display.set_mode((longueur, hauteur))           # charge la fenêtre de hauteur 465 et de longeur 800
    
    labyrinthe = pygame.image.load("photo_map.png")                   # sert à importer une image (ici la map)
    labyrinthe_masque = pygame.mask.from_surface(labyrinthe)
    
    screen = screen.convert()                                       # convertit l'image
    screen.blit(image1, (0,0))                                      # affiche l'image
    
    interface()                                                     # affiche l'interface
    
    musique()                                                       # lance la musique
        
    while True:                                                     # Permet de stopper le programme donc de mettre fin au jeu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit ()
            if event.type == pygame.KEYDOWN:
                continuer = False 
         
        
        pygame.key.set_repeat(1,20)
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
                
        pygame.display.flip()
        
        


        
                                                                        # permet le déplacements du personnages dans differentes direct
    
def temps():                                                                        # création d'un minuteur/chronomètre
    chrono = False
    start_ticks=pygame.time.get_ticks()#lance le chrono
    while not chrono :
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds<10:
            print(seconds)
        else :
            chrono = True
            fin()
            
 

def musique():                                                                      #création d'une fonction de musique qui se lance lors du lancement de la partie
    pygame.mixer.music.load('muique pour projet NSI.ogg')
    pygame.mixer.music.play()
    Sound.play(loops=1, maxtime=0, fade_ms=0)
    
    
def interface():                                                                    # interface de bienvenue avec l'explication du but du jeu et des règles
    police = pygame.font.SysFont("ubuntu",17)
    label = police.render('Bienvenue dans ',True,(0,0,0))
    cran.blit(label,(0,0))     
    if event.key == pygame.K_SPACE:
      
      temps()
        
        
   
def fin() :                                                                         #affiche une image avec écrit game over lors de la fin du temps a partie / lorsque le joueur à perdu    
    screen = pygame.display.set_mode((longueur, hauteur))
    image2 = pygame.image.load('game_over.jpeg')
    image2 = image.convert()
    screen. blit(image, (82,50))
    pygame.display.flip()
