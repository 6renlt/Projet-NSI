import pygame
from pygame.locals import *
pygame.init()

longueur = 805
hauteur  = 485

pygame.mixer.music.load('muique pour projet NSI.ogg')            # importe la musique
pygame.mixer.music.play(loops= -1, start=0.0, fade_ms=5000)      # Activation de la musique en boucle avec un fondu sonore
pygame.mixer.music.set_volume(0.2)                               # Diminue le volume de la musique 


ecran = pygame.display.set_mode((longueur, hauteur))             # charge la fenêtre de hauteur 465 et de longeur 800

pygame.key.set_repeat(1,20)                                      # Permet de répéter la touche quand elle est maintenu


labyrinthe = pygame.image.load("photo_map.png")                  # sert à importer la map
labyrinthe_masque = pygame.mask.from_surface(labyrinthe)         # créer un masque sur les murs de la map


perso = pygame.image.load("Fred.png")                            # Importation personnage
perso = pygame.transform.scale(perso, (28,28))                   # Dimunution de la taille
perso_rect = pygame.Rect(10,10,28,28)                            # Création d'un rectangle sur le personnage
perso_masque = pygame.mask.from_surface(perso)                   # Création d'un masque sur le personnage


objet = pygame.image.load("Foulard.png")                         # Importation de l'objet
objet = pygame.transform.scale(objet, (40,40))                   # Dimunution de la taille
objet_rect = pygame.Rect(420,200,20,20)                          # Création d'un rectangle sur l'objet

objetRecupere = False                                            # Variable de vérification de la récupération de l'objet

arrive = pygame.image.load("Arrivé.png")                         # Importation de l'arrivé
arrive = pygame.transform.scale(arrive, (58,40))                 # Dimunution de la taille
arrive_rect = pygame.Rect(410,10,35,35)                          # Création d'un rectangle sur l'arrivé

police = pygame.font.SysFont("Arial", 15)                        # Établi la police d'écriture

debut = pygame.time.get_ticks()                                  # Activation du chronomètre
tempActif = True                                                 # Booléen de marche du chronomètre

hardMode = False                                                 # Booléen activation du mode difficile

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            ancienne_position = perso_rect.copy()                     # Récupération de la position avant mouvement du personnage
            if event.key == pygame.K_RIGHT:                           # Déplacement droit
                perso_rect.move_ip((5,0))
                perso = pygame.image.load("Fred.png")            
                perso = pygame.transform.scale(perso, (28,28))
                perso = pygame.transform.flip(perso, True, False)     # Orientation personnage vers mouvement
            elif event.key == pygame.K_UP:                            # Déplacement haut
                perso_rect.move_ip((0,-5))
            elif event.key == pygame.K_LEFT:                          # Déplacement gauche
                perso_rect.move_ip((-5,0))
                perso = pygame.image.load("Fred.png")            
                perso = pygame.transform.scale(perso, (28,28))
            elif event.key == pygame.K_DOWN:                          # Déplacement bas
                perso_rect.move_ip((0,5))
            elif event.key == pygame.K_h :                            # Activation ou désactivation du mode difficile
                if hardMode == True :
                    hardMode = False
                else :
                    hardMode = True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                
    if labyrinthe_masque.overlap(perso_masque, perso_rect.topleft) != None:    # Vérification des collision entre masque perso. et murs
        if hardMode == False:
             perso_rect = ancienne_position                                    # Annulation du mouvement du personnage si mode difficile en False
        else:
            perso = pygame.image.load("Fred.png")                              # Réapparition de départ car mode difficile en True
            perso = pygame.transform.scale(perso, (28,28))
            perso_rect = pygame.Rect(10,10,28,28)
            perso_masque = pygame.mask.from_surface(perso)
    if perso_rect.colliderect(objet_rect):                                     # Vérification de collision entre rectangle objet et perso.
        objet_rect = perso_rect                                                # Attribution de la position objet à la position du personnage
        objetRecupere = True                                                   # Booléen de récupération de l'objet en True
            
                
            
    ecran.fill((255, 255, 255))                                                # Affichage des différent objet
    ecran.blit(labyrinthe, (0,0))
    ecran.blit(arrive, arrive_rect)
    ecran.blit(objet, objet_rect)
    ecran.blit(perso, perso_rect)
    
    if perso_rect.colliderect(arrive_rect) and objetRecupere == True:                    # Vérification collision personnage arrivé + booléen en True 
            ecran.fill((0,0,0))                                                          # Écran noir
            if tempActif == True:                                                        # Récupère le chronomètre si booléen encore en True
                temps = pygame.time.get_ticks()/1000
                temps = str(temps)
            info = police.render("Pressez 'Echap' pour quitter", 1 , (255,255,255))      # Écritures de fin
            seconde = police.render("secondes", 1 , (255,255,255))
            resultat = police.render(temps, 1 , (255,255,255))
            ecran.blit(seconde, (404,242))                                               # Affichage des écritures
            ecran.blit(info, (315,370))
            ecran.blit(resultat, (350,242))
            tempActif = False                                                            # Booléen du chrono mis en False pour l'arrêter 
            
            


    pygame.display.flip()
