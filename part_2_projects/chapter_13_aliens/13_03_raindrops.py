#5, rainfall sim

import pygame
from random import randint

# Initialize Pygame
pygame.init()

class Raindrop:
    def __init__(self):
        # Randomize the initial position of the raindrop
        self.x = randint(0, 800)
        self.y = 0
        self.image = pygame.image.load("assets/raindrop.png")
        self.image = pygame.transform.scale(self.image,(25,25))
        self.speed = randint(3, 5)  

    def update(self):

        self.y += self.speed
        # If the raindrop goes off the screen, reset its position
        if self.y > 600:  
            self.y = 0
            self.x = randint(0, 800)

    def draw(self, screen):
        # Draw the raindrop on the screen
        screen.blit(self.image, (self.x, self.y))

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainfall Simulation")

# List to store raindrops
raindrops = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a blue color
    screen.fill((0, 0, 255))

   
    
    raindrops.append(Raindrop())

    # Update and draw all raindrops
    for raindrop in raindrops:
        raindrop.update()
        raindrop.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
