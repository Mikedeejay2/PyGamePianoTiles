import pygame
import menu
import game

monitor_width = pygame.display.Info().current_w
monitor_height = pygame.display.Info().current_h
screen_width = 0
screen_height = 0
screen: pygame.surface.Surface
fullscreen = False
fps = 60
scene = "menu"
word_list = []

# Load word list from a file
with open("wordlist.txt", "r") as file:
    for line in file:
        word_list.append(line.strip())

# Set the resolution of the screen
def set_res(width, height):
    global screen_width, screen_height
    screen_width = width
    screen_height = height
    menu.set_elements()
    game.set_elements()
    return pygame.display.set_mode((width, height))

# Toggle fullscreen mode
def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((screen_width, screen_height))