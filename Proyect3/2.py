import cv2
import pygame
from pygame.locals import *

# Inicializar Pygame
pygame.init()

# Configurar la ventana de Pygame
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame to OpenCV with Square')

# Crear un surface Pygame con un círculo
pygame_surface = pygame.Surface((width, height))
pygame.draw.circle(pygame_surface, (255, 0, 0), (width // 2, height // 2), 50)  # Círculo rojo

# Convertir el surface de Pygame a una matriz NumPy
pygame_image = pygame.surfarray.array3d(pygame_surface)
cv_image = cv2.cvtColor(pygame_image, cv2.COLOR_RGB2BGR)

# Dibujar un cuadrado sobre el círculo usando OpenCV
cv2.rectangle(cv_image, (width // 2 - 25, height // 2 - 25), (width // 2 + 25, height // 2 + 25), (0, 255, 0), 2)

# Convertir la matriz NumPy de nuevo a un surface de Pygame
modified_pygame_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
modified_pygame_surface = pygame.surfarray.make_surface(modified_pygame_image)

while True:
    # Mostrar el frame modificado en la ventana de Pygame
    screen.blit(modified_pygame_surface, (0, 0))
    pygame.display.flip()

    # Manejar eventos de Pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

