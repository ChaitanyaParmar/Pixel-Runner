import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) # width, height
pygame.display.set_caption('Runner') # title
clock = pygame.time.Clock() 

# test_surface = pygame.Surface((100, 200)) # width, height
# test_surface.fill('Red') # color

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface, (200,100)) # surface, position  # block image transfer # Origin point is in top left

    pygame.display.update()
    clock.tick(60) # shouldn't run faster than 60 time per second 
