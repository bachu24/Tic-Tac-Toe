# Example file showing a basic pygame "game loop"
import pygame

# pygame setups
pygame.init()
WINDOW_WIDTH = 800 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True

def load_icons(path,resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)
    
grid=load_icons('img/grid.png',[WINDOW_WIDTH,WINDOW_WIDTH])
iconX=load_icons('img/x-icon.png',[WINDOW_WIDTH//3,WINDOW_WIDTH//3])
iconO=load_icons('img/o-icon.png',[WINDOW_WIDTH//3,WINDOW_WIDTH//3])
 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    
    screen.blit(grid,(0,0)) 
    screen.blit(iconX,(0,0))
    screen.blit(iconO,(WINDOW_WIDTH//3,WINDOW_WIDTH//3))
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()