# 7, improved sideways shooter

import pygame
import random

pygame.init()

# Initialize screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sideways Shooter")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player class
class Player:
    def __init__(self):
        self.x = 20
        self.y = height // 2
        self.image = pygame.image.load("assets/ship.png")
        self.velocity = 10
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw_on_screen(self, screen):
        rotated_image = pygame.transform.rotate(self.image, 270)
        screen.blit(rotated_image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)  

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15
        self.width = 10
        self.height = 5
        self.color = RED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.x += self.speed 
        self.rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Alien class
class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Game objects
player = Player()
bullets = []  
aliens = []  

# Spawn alien function
def spawn_alien():
    x = width + 50
    y = random.randint(0, height - 50)  
    aliens.append(Alien(x, y))

# Main game loop
clock = pygame.time.Clock()
running = True
alien_spawn_time = 0  

while running:
    clock.tick(60)  
    alien_spawn_time += 1

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.y = max(0, player.y - player.velocity)
            if event.key == pygame.K_DOWN:
                player.y = min(height - player.rect.height, player.y + player.velocity)
            if event.key == pygame.K_SPACE:
                # Create a bullet at the player's current position
                bullets.append(Bullet(player.rect.right, player.rect.centery))

    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        if bullet.x > width:  
            bullets.remove(bullet)

    # Update aliens
    for alien in aliens[:]:
        alien.update()
        if alien.x < -50:
            aliens.remove(alien)

        # Check for collisions
        for bullet in bullets[:]:
            if alien.rect.colliderect(bullet.rect):
                aliens.remove(alien)
                bullets.remove(bullet)
                break

    # Spawn aliens every 120 frames (~2 seconds at 60 FPS)
    if alien_spawn_time > 120:
        spawn_alien()
        alien_spawn_time = 0

    # Drawing
    screen.fill(BLUE)  
    player.draw_on_screen(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for alien in aliens:
        alien.draw(screen)

    pygame.display.flip()

pygame.quit()
