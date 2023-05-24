import pygame

# pygame setup
pygame.init()

import variables

variables.screen = variables.set_res(1280, 720)
clock = pygame.time.Clock()
running = True

import menu

while running:
    variables.set_res(variables.screen_width + 1, variables.screen_height + 1)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    variables.screen.fill("blue")

    # RENDER YOUR GAME HERE
    menu.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(variables.fps)  # limits FPS to 60

pygame.quit()