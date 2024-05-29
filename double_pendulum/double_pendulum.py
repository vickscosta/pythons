'''simulation of a double pendulum
Env : python 3.12 planets'''

import pygame
import numpy as np
import random

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
BLUE=(100,149,237)
RED=(188,39,50)
DARK_GREY=(80,78,81)
ORANGE=(255,127,0)
PINK=(255,192,203)
GREEN=(0,255,0)
ROSE=(255,0,128)

# Pygame
pygame.init()

# Screen Settings
width, height = 800, 640
screen = pygame.display.set_mode((width, height))

# Pendulum Settings
LENGHT1 = 100 # first
LENGHT2 = 150 # second
MASS1 = 5
MASS2 = 3
# Initial Positions
angle1 = np.pi * 1.5
angle2 = np.pi / 3

angular_velocity1 = 0.2
angular_velocity2 = 0
GRAVITY = 1

# Time step - Like FPS
DELTA_T = 0.2
DRAW_LIM=5000

# Pygame Loop
running = True
updated_points_1 = []
updated_points_2 = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
      # Clear the screen
    screen.fill(BLACK)

    # EQUATIONS OF MOTION

    # Calculating accelerations...
    numerator1 = -GRAVITY * (2 * MASS1 + MASS2) * np.sin(angle1)
    numerator2 = -MASS2 * GRAVITY * np.sin(angle1 - 2 * angle2)
    numerator3 = -2 * np.sin(angle1 - angle2) * MASS2
    numerator4 = angular_velocity2**2 * LENGHT2 + angular_velocity1**2 * LENGHT1 * np.cos(angle1 - angle2)
    denominator = LENGHT1 * (2 * MASS1 + MASS2 - MASS2 * np.cos(2 * angle1 - 2 * angle2))
    angular_acceleration1 = (numerator1 + numerator2 + numerator3 * numerator4) / denominator

    numerator1 = 2 * np.sin(angle1 - angle2)
    numerator2 = angular_velocity1**2 * LENGHT1 * (MASS1 + MASS2)
    numerator3 = GRAVITY * (MASS1 + MASS2) * np.cos(angle1)
    numerator4 = angular_velocity2**2 * LENGHT2 * MASS2 * np.cos(angle1 - angle2)
    denominator = LENGHT2 * (2 * MASS1 + MASS2 - MASS2 * np.cos(2 * angle1 - 2 * angle2))
    angular_acceleration2 = (numerator1 * (numerator2 + numerator3 + numerator4)) / denominator

    # Changings the velocities and angles...
    angular_velocity1 += angular_acceleration1 * DELTA_T
    angular_velocity2 += angular_acceleration2 * DELTA_T
    angle1 += angular_velocity1 * DELTA_T
    angle2 += angular_velocity2 * DELTA_T

    # Calculating the mod of the angle, to avoid "big number" errors.
    angle1 = angle1 % (2 * np.pi)
    angle2 = angle2 % (2 * np.pi)

    # Calculating balls positions
    x1 = LENGHT1 * np.sin(angle1)
    y1 = LENGHT1 * np.cos(angle1)
    x2 = x1 + LENGHT2 * np.sin(angle2)
    y2 = y1 + LENGHT2 * np.cos(angle2)

    # Drawing the lines and balls.
    pygame.draw.line(screen, WHITE, (width/2, height/2), (width/2 + x1, height/2 + y1))
    pygame.draw.line(screen, WHITE, (width/2 + x1, height/2 + y1), (width/2 + x2, height/2 + y2))
    pygame.draw.circle(screen, BLUE, ((width/2 + x1), (height/2 + y1)), 10)
    pygame.draw.circle(screen, GREEN, ((width/2 + x2), (height/2 + y2)), 10)

    #Trail
    updated_points_1.append((width/2 + x1, height/2 + y1))
    updated_points_2.append((width/2 + x2, height/2 + y2))

    if len(updated_points_1)>1:
        if len(updated_points_1)<DRAW_LIM:
            pygame.draw.lines(screen, ORANGE, False, updated_points_1, 2)
        else:
            updated_points_1=updated_points_1[-DRAW_LIM:]
            pygame.draw.lines(screen, ORANGE, False, updated_points_1, 2)

    if len(updated_points_2)>1:
        if len(updated_points_2)<DRAW_LIM:
            pygame.draw.lines(screen, GREEN, False, updated_points_2, 3)
        else:
            updated_points_2=updated_points_2[-DRAW_LIM:]
            pygame.draw.lines(screen, GREEN, False, updated_points_2, 3)

    # Update the display
    pygame.display.flip()

    # Like - FPS
    pygame.time.delay(5)

# Quit Pygame
pygame.quit()