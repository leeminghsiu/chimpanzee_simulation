import pygame
pygame.font.init()

FPS = 24
font = pygame.font.Font('freesansbold.ttf', 18)
font2 = pygame.font.Font('freesansbold.ttf', 25)
WIDTH, HEIGHT = 720, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("chimp_simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)   # dot color
RED = (255, 192, 203)   # territory color
BLUE = (120, 110, 255)  # square color

DOT_QUANTITY = 15    # numbers of males
SQUARE_QUANTITY = 25    # numbers of female
DOT_SPEED = 2 # male speed
SQUARE_SPEED = 3    # female speed
DISTANCE_BETWEEN_SQUARE = 10    # female personal space
COMBAT_VALUE_CENTER = 60
COMBAT_VALUE_SPREAD = 50
CV_IMPORTANCE_TO_FEMALE = 100     # how much do female care about power
                                # (to the power of closest_dot.combat_value)

