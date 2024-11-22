# 2, random grib of stars

import pygame
from random import randint


# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load image
image = pygame.image.load("assets/star.png")

# Image dimensions
image_width = 100
image_height = 100
image = pygame.transform.scale(image, (image_width, image_height))

# can adjust rows/cols
grid_rows = 4
grid_cols = 4

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) # can adjust bg color

    for row in range(grid_rows):
        for col in range(grid_cols):
            # Calculate spacing each time during main loop
            x_spacing = randint(0,50)
            y_spacing = randint(0,50)
            
            x = x_spacing * (col + 1) + image_width * col
            y = y_spacing * (row + 1) + image_height * row
            screen.blit(image, (x, y))

    pygame.display.flip()

pygame.quit()