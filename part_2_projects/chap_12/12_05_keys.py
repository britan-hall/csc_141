import pygame

pygame.init()

width = 200
height = 100

screen = pygame.display.set_mode((width, height))

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: 
                run = False
                pygame.quit() 
                quit() 

            if event.type == pygame.KEYDOWN: 
                 print(pygame.key.name(event.key))
                 
    screen.fill((0, 0, 255)) 

    pygame.display.flip()

pygame.quit()