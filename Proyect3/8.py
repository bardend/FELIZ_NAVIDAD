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

# Inicializar variables
num_circles = 30
circle_radius = 20

# Crear fuente para renderizar texto más grande y centrado
font = pygame.font.Font(None, 72)  # Tamaño de la fuente aumentado
font.set_bold(True)  # Texto en negrita

def draw_connected_circles(surface, circle_positions, circle_radius):
    # Colores permitidos: rojo, azul, verde, amarillo
    allowed_colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]

    # Dibujar círculos
    for i in range(len(circle_positions)):
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

    # Limpiar la superficie con un color de fondo para borrar los círculos y texto anteriores
    background_color = (0, 0, 0)  # Puedes ajustar el color de fondo según tus preferencias

    pygame_surface.fill(background_color)

    circle_positions = [(np.random.randint(0, viewport[0]), np.random.randint(0, viewport[1])) for _ in range(num_circles)]

    # Dibujar círculos y una línea conectando todos los círculos
    draw_connected_circles(pygame_surface, circle_positions, circle_radius)

    # Posicionar la imagen del árbol en la mitad de la ventana
    cv_image = Pygame_to_cv2(pygame_surface)

    cv2.imshow('Modified Image', cv_image)
    cv2.waitKey(1)

    # Realizar la segmentación
    xd = Segmentation(cv_image)

    # Renderizar texto "FELIZ NAVIDAD" más grande, blanco y centrado
    text_surface = font.render("FELIZ NAVIDAD", True, (255, 255, 255))  # Color blanco
    text_rect = text_surface.get_rect(center=(viewport[0] // 2, viewport[1] // 2))  # Posicionar en el centro

    # Blit del texto en la superficie principal
    pygame_surface.blit(text_surface, text_rect)

    # Convertir la superficie de Pygame a una matriz NumPy después de agregar el texto
    cv_image_with_text = Pygame_to_cv2(pygame_surface)

    modified_pygame_surface = Cv2_to_pygame(cv_image_with_text)

    pygame.display.get_surface().blit(modified_pygame_surface, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1000)

