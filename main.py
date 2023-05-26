import pygame

# pygame setup
pygame.init()

import variables

variables.screen = variables.set_res(1280, 720)
clock = pygame.time.Clock()
running = True

import menu
import game

while running:
    # Test if surfaces resize correctly by constantly increasing screen size
    # variables.set_res(variables.screen_width + 1, variables.screen_height + 1)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif variables.scene == "menu":
            menu.on_event(event)
        elif variables.scene == "game":
            game.on_event(event)

    # fill the screen with a color to wipe away anything from last frame
    variables.screen.fill("SteelBlue")

    # RENDER YOUR GAME HERE
    if variables.scene == "menu":
        menu.draw()
    elif variables.scene == "game":
        game.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(variables.fps)  # limits FPS

pygame.quit()