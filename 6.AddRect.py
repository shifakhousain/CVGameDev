"""
Rect

    con detect Collision
    con access x and y points

    two ways of creating a rect
    1. pygame.Rect(x,y,width,height
    2. surface.get_rect() # create rect around a surface/image
"""

# Import
import pygame

# Initialize
pygame.init()

# Create Window/Display
width,height = 1280 , 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awasome Game")

#Initialize clock for Fps
fps = 30
clock = pygame.time.Clock()

# Load Images
imageBackground = pygame.image.load("../Resources/background.jpg").convert()
imagBaloonRed   = pygame.image.load("../Resources/10baloon.png").convert_alpha()
rectBalloon = imagBaloonRed.get_rect()

# Rect
rectNew = pygame.Rect(500,0,200,200)



# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.QUIT()

    # Apply Logics
    print(rectBalloon.colliderect(rectNew))
    rectBalloon.x += 2



    window.blit(imageBackground,(0,0))
   # pygame.draw.rect(window, (0, 255, 0), rectBalloon)
   # pygame.draw.rect(window, (0, 255, 0), rectNew)
    window.blit(imagBaloonRed, rectBalloon)

    #Update Display
    pygame.display.update()
    # Set fps
    clock.tick(fps)
