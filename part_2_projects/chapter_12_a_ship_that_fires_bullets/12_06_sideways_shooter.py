# 4, shooting 

import pygame

pygame.init()

class Player:
    def __init__(self):
        self.x = 20
        self.y = 300
        self.image = pygame.image.load("assets/ship.png")
        self.velocity = 10
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw_on_screen(self, screen):
        rotated_image = pygame.transform.rotate(self.image, 270)
        screen.blit(rotated_image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)  # Update rect position


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15
        self.width = 10
        self.height = 5
        self.color = (255, 0, 0)

    def update(self):
        self.x += self.speed  # Move bullet to the right

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# Initialize Pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("12_06")

player = Player()
bullets = []  # List to track bullets
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # Limit to 60 FPS

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.y -= player.velocity
            if event.key == pygame.K_DOWN:
                player.y += player.velocity
            if event.key == pygame.K_SPACE:
                # Create a bullet at the player's current position
                bullets.append(Bullet(player.rect.centerx, player.rect.centery))

    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        if bullet.x > width:  # Remove bullets that move off-screen
            bullets.remove(bullet)

    # Drawing
    screen.fill((0, 0, 255))  # Clear screen with blue
    player.draw_on_screen(screen)

    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()

pygame.quit()
