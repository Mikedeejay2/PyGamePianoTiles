import pygame
import menu
import game
import settings
import background
import how_to_play

monitor_width = pygame.display.Info().current_w
monitor_height = pygame.display.Info().current_h
screen_width = 0
screen_height = 0
screen: pygame.surface.Surface
fullscreen = False
fps = 60
scene = "menu"
word_list = []

supported_resolutions = (
    (640, 360),
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1366, 768),
    (1536, 864),
    (1600, 900),
    (1600, 1200),
    (1920, 1080),
    (2048, 1152),
    (2560, 1440),
    (3840, 2160)
)

# Load word list from a file
with open("wordlist.txt", "r") as file:
    for line in file:
        word_list.append(line.strip())

# Set the resolution of the screen
def set_res(width, height):
    global screen_width, screen_height
    screen_width = width
    screen_height = height
    result = pygame.display.set_mode((width, height))
    menu.set_elements()
    game.set_elements()
    settings.set_elements()
    background.set_elements()
    how_to_play.set_elements()
    return result

# Toggle fullscreen mode
def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((screen_width, screen_height))