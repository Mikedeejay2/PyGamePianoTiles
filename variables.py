import pygame
import menu

monitor_width = pygame.display.Info().current_w
monitor_height = pygame.display.Info().current_h
screen_width = 0
screen_height = 0
screen: pygame.surface.Surface
fullscreen = False
fps = 60

def set_res(width, height):
    global screen_width, screen_height
    screen_width = width
    screen_height = height
    menu.set_elements()
    return pygame.display.set_mode((width, height))

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((screen_width, screen_height))