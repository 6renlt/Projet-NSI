import pygame
from pygame.locals import *
pygame.init()

longueur = 805
hauteur  = 485

ecran = pygame.display.set_mode((longueur, hauteur))
pygame.key.set_repeat(1,20)

labyrinthe = pygame.image.load("photo_map.png")
labyrinthe_masque = pygame.mask.from_surface(labyrinthe)

perso = pygame.image.load("Fred.png")
perso = pygame.transform.scale(perso, (20,20))

perso_rect = pygame.Rect(10,10,20,20)
perso_masque = pygame.mask.from_surface(perso)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            ancienne_position = perso_rect.copy()
            print("avant mouvement", ancienne_position, type(ancienne_position))
            if event.key == pygame.K_RIGHT:
                perso_rect.move_ip((5,0))
            elif event.key == pygame.K_UP:
                perso_rect.move_ip((0,-5))
            elif event.key == pygame.K_LEFT:
                perso_rect.move_ip((-5,0))
            elif event.key == pygame.K_DOWN:
                perso_rect.move_ip((0,5))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
            print("après mouvement", perso_rect)
            if labyrinthe_masque.overlap(perso_masque, perso_rect.topleft) != None:
                print('collision')
                perso_rect = ancienne_position
                print("changement", perso_rect)
            
    ecran.fill((255, 255, 255))
    ecran.blit(labyrinthe, (0,0))
    ecran.blit(perso, perso_rect)
#     pygame.draw.rect(ecran, "blue", perso_rect)
    
    pygame.display.flip()