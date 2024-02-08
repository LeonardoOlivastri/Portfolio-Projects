#pip install pygame

import pygame
import random
from blob import Blob
import numpy as np
import logging

#Definizione del numero di blob a schermo
STARTING_BLUE_BLOBS = 50
STARTING_RED_BLOBS = 50
STARTING_GREEN_BLOBS = 50

#Parametri da passare per creare i blob
WIDTH = 800
HEIGHT = 600
SIZE_MULTIPLIER = 2
MOVEMENT_MULTIPLIER = 3

#Colori che verranno usati nel gioco
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT)) #creazione display di gioco
pygame.display.set_caption("Blob World") #titolo del gioco
clock = pygame.time.Clock() #definizione dei frame al secondo

#se la distanza tra due blob è inferiore alla somma delle loro size, allora si stanno toccando
def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

#definire il comportamento dei blob di colori diversi quando si toccano
def handle_collisions(blob_list):
    blues, reds, greens = blob_list 
    color_combinations = [(blues, reds), (blues, greens), (reds, greens)]
    for color_pair in color_combinations:
        for blob_id, blob_1 in color_pair[0].copy().items():
            for other_blob_id, blob_2 in color_pair[1].copy().items():
                logging.debug('Checking if blobs touching {} + {}'.format(str(blob_1), str(blob_2)))
                if blob_1 == blob_2: #evitare che il blob tocchi sé stesso
                    pass
                else:
                    if is_touching(blob_1, blob_2):
                        blob_1 + blob_2
                        if blob_2.size <= 0:
                            del color_pair[1][other_blob_id]
                        if blob_1.size <= 0:
                            del color_pair[0][blob_id]
    
    return blues, reds, greens

#funzione per stampare a video i processi
def draw_environment(blob_list):
    game_display.fill(WHITE) #colorare tutto lo schermo di bianco
    blues, reds, greens = handle_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size) #disegnare il blob
            blob.move() #muoverlo
            blob.check_bounds() #vedere se è arrivato al limite dello schermo

    pygame.display.update()
    return blues, reds, greens

def main():
    blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT, SIZE_MULTIPLIER, MOVEMENT_MULTIPLIER) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED,WIDTH,HEIGHT, SIZE_MULTIPLIER, MOVEMENT_MULTIPLIER) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([Blob(GREEN,WIDTH,HEIGHT, SIZE_MULTIPLIER, MOVEMENT_MULTIPLIER) for i in range(STARTING_GREEN_BLOBS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs,red_blobs,green_blobs])
        clock.tick(60) #60 FPS

if __name__ == '__main__':
    main()