import pygame
import variables
import utils

text_color = "white"

def set_elements():
    global title_surf, title_rect
    # TODO: Replace with image
    title_surf = pygame.surface.Surface((variables.screen_width / 2, variables.screen_height / 6))
    title_surf.fill("white")
    title_rect = utils.get_rect(title_surf, 50, 20)

    global text_font
    # TODO: Add Font file
    text_font = pygame.font.Font(None, int(variables.screen_width / 20))

    global settings_surf, settings_rect
    settings_surf = text_font.render("Settings", True, text_color)
    settings_rect = utils.get_rect(settings_surf, 50, 45)

    global play_surf, play_rect
    play_surf = text_font.render("Play", True, text_color)
    play_rect = utils.get_rect(play_surf, 50, 60)

    global credits_surf, credits_rect
    credits_surf = text_font.render("Credits", True, text_color)
    credits_rect = utils.get_rect(credits_surf, 50, 75)


def draw():
    variables.screen.blit(title_surf, title_rect)
    variables.screen.blit(settings_surf, settings_rect)
    variables.screen.blit(play_surf, play_rect)
    variables.screen.blit(credits_surf, credits_rect)