import cv2
import pygame
from pygame.locals import *
import numpy as np
from Tools import *
from Segmentation import *

# Inicializar Pygame
pygame.init()
viewport = (1200, 800)  # Nuevo tamaño de la ventana
pygame.display.set_mode(viewport)

# Generar posiciones aleatorias fijas para los círculos
num_circles = 30
circle_positions = [(np.random.randint(0, viewport[0]), np.random.randint(0, viewport[1])) for _ in range(num_circles)]

# Crear fuente para renderizar texto
font = pygame.font.Font(None, 36)  # Puedes ajustar el tamaño de la fuente

def draw_connected_circles(surface, circle_positions, circle_radius):
    # Colores permitidos: rojo, azul, verde, amarillo
    allowed_colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]

    # Dibujar círculos
    for i in range(num_circles):
        color = allowed_colors[i % len(allowed_colors)]  # Ciclar entre los colores permitidos
        pygame.draw.circle(surface, color, circle_positions[i], circle_radius)

    # Conectar todos los círculos con una sola línea
    line_color = (255, 255, 255)  # Color de línea blanco
    pygame.draw.lines(surface, line_color, False, circle_positions, 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame_surface = pygame.Surface(viewport)

    # Dibujar círculos y una línea conectando todos los círculos
    draw_connected_circles(pygame_surface, circle_positions, circle_radius=20)

    # Posicionar la imagen del árbol en la mitad de la ventana
    cv_image = Pygame_to_cv2(pygame_surface)

    cv2.imshow('Modified Image', cv_image)
    cv2.waitKey(1)

    xd = Segmentation(cv_image)

    modified_pygame_surface = Cv2_to_pygame(cv_image)

    # Renderizar texto "FELIZ NAVIDAD"
    text_surface = font.render("FELIZ NAVIDAD", True, (255, 255, 255))  # Color blanco
    text_rect = text_surface.get_rect(center=(viewport[0] // 2, viewport[1] - 50))  # Posicionar en la parte inferior central

    # Blit del texto en la superficie principal
    modified_pygame_surface.blit(text_surface, text_rect)

    pygame.display.get_surface().blit(modified_pygame_surface, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1000)

