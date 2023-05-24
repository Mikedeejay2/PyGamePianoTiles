import pygame
import variables

title_surf = None
title_rect = None


def set_elements():
    global title_surf, title_rect
    title_surf = pygame.surface.Surface((variables.screen_width / 2, variables.screen_height / 4))
    title_surf.fill("white")
    title_rect = title_surf.get_rect(center = (variables.screen_width / 2, variables.screen_height / 4))

def draw():
    variables.screen.blit(title_surf, title_rect)