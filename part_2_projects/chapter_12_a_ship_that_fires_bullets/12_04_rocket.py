# 2, movement

import pygame

pygame.init()

class Player:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.image = pygame.image.load("assets/ship.png")
        self.velocity = 2
    def draw_on_screen(self):
        screen.blit(self.image,(self.x,self.y))
        

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
  
    for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: 
                run = False
                pygame.quit() 
                quit() 

            if event.type == pygame.KEYDOWN: 

                if event.key == pygame.K_LEFT: 
                    player.x -= player.velocity 

                if event.key == pygame.K_RIGHT: 
                    player.x += player.velocity 

                if event.key == pygame.K_UP: 
                    player.y -= player.velocity 
 
                if event.key == pygame.K_DOWN: 
                    player.y += player.velocity 

            pygame.display.update() 
