import cv2
import pygame
from pygame.locals import *
import numpy as np
from Tools import *


def Pygame_to_cv2(pygame_surface) :
    pygame_array = pygame.surfarray.array3d(pygame_surface)
    cv_image = np.copy(pygame_array)

    return cv_image


def Cv2_to_pygame(cv_image) :
    modified_pygame_surface = pygame.surfarray.make_surface(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))
    return modified_pygame_surface
