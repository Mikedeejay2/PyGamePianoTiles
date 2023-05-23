import pygame

# pygame setup
pygame.init()

screen_width = 1280
screen_height = 720

monitor_width = pygame.display.Info().current_w
monitor_height = pygame.display.Info().current_h

fullscreen = False

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def set_res(width, height):
    global screen_width, screen_height
    screen_width = width
    screen_height = height
    pygame.display.set_mode((width, height))

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((screen_width, screen_height))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()