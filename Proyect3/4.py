import cv2
import pygame
from pygame.locals import *
import numpy as np
from Tools import *

# Inicializar Pygame
pygame.init()
viewport = (640, 480)
pygame.display.set_mode(viewport)

def draw_circle(surface):
    # Dibujar un círculo en Pygame
    pygame.draw.circle(surface, (255, 0, 0), (320, 240), 50)
       

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Crear una superficie de Pygame y dibujar el círculo en ella
    pygame_surface = pygame.Surface(viewport)
    draw_circle(pygame_surface)

    # Crear una imagen de OpenCV copiando la matriz NumPy
    cv_image = Pygame_to_cv2(pygame_surface)

    # Dibujar un rectángulo en OpenCV
    cv2.rectangle(cv_image, (270, 190), (370, 290), (0, 255, 0), 2)

    # Mostrar la imagen de OpenCV
    cv2.imshow('Modified Image', cv_image)
    cv2.waitKey(1)

    # Convertir la imagen de OpenCV a una superficie de Pygame
    modified_pygame_surface = Cv2_to_pygame(cv_image)

    # Mostrar la superficie modificada en la ventana de Pygame
    pygame.display.get_surface().blit(modified_pygame_surface, (0, 0))
    pygame.display.flip()

