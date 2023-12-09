import pygame
import cv2
import numpy as np
from pygame.locals import *

pygame.init()

# Configurar la ventana de Pygame
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Círculo en Pygame")

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar un círculo en Pygame
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

    pygame.display.flip()

    # Capturar el frame de Pygame y mostrarlo en OpenCV
    image = pygame.surfarray.array3d(screen)
    cv_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    #cv2.imshow('Círculo en OpenCV', cv_image)

    print(cv_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pygame.quit()
cv2.destroyAllWindows()

