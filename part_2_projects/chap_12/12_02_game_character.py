import pygame

pygame.init()

class Player:
    def __init__(self):
        self.position = (400,300)
        self.image = pygame.image.load("assets/ship.png")
    def draw_on_screen(self):
        screen.blit(self.image,self.position)
        

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
player  = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255)) 
    Player.draw_on_screen(player)
    pygame.display.flip()

pygame.quit()