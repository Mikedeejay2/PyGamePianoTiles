import pygame
import variables

def get_rect(surface, percent_width, percent_height):
    return surface.get_rect(center = (
        variables.screen_width * (percent_width / 100), 
        variables.screen_height * (percent_height / 100)
        ))