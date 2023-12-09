from math import cos, sin

import cv2
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Initialize Pygame and OpenGL
pygame.init()
viewport = (640, 480)
pygame.display.set_mode(viewport, DOUBLEBUF | OPENGL)

# Set up perspective
glOrtho(0, viewport[0], viewport[1], 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

def draw_circle():
    # Draw a circle in OpenGL
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0, 0)
    glVertex2f(320, 240)  # Center of the circle
    for i in range(360):
        radians = i * (3.14159 / 180.0)
        x = 320 + 50 * cos(radians)
        y = 240 + 50 * sin(radians)
        glVertex2f(x, y)
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Draw the circle in OpenGL
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle()
    pygame.display.flip()

    # Capture the content of the Pygame window and convert it to OpenCV
    pixels = glReadPixels(0, 0, 640, 480, GL_RGB, GL_UNSIGNED_BYTE)
    pixels_array = np.frombuffer(pixels, dtype=np.uint8).reshape((480, 640, 3))
    cv_image = cv2.cvtColor(pixels_array, cv2.COLOR_RGB2BGR)

    # Draw a square in OpenCV
    cv2.rectangle(cv_image, (270, 190), (370, 290), (0, 255, 0), 2)

    # Convert the OpenCV image back to a Pygame surface
    modified_pygame_surface = pygame.image.fromstring(cv2.flip(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB), 1).tobytes(), (640, 480), 'RGB')

    # Show the modified frame in the Pygame window
    glClear(GL_COLOR_BUFFER_BIT)
    glRasterPos2i(0, 0)
    glDrawPixels(640, 480, GL_RGB, GL_UNSIGNED_BYTE, pixels)
    pygame.display.flip()

