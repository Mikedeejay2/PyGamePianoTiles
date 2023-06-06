import pygame
import variables

background_color1 = (47, 74, 102)
background_color2 = (59, 93, 128)
background_color3 = (70, 112, 153)
background_color4 = (82, 130, 179)
background_color5 = (106, 168, 230)
background_color6 = (117, 186, 255)

background_rect1 = None
background_rect2 = None
background_rect3 = None
background_rect4 = None
background_rect5 = None
background_rect6 = None

def set_elements():
    global background_rect1, background_rect2, background_rect3, background_rect4, background_rect5, background_rect6
    background_rect1 = pygame.rect.Rect(0, 0, variables.screen_width, variables.screen_height)
    background_rect2 = pygame.rect.Rect(0, variables.screen_height * (1/11), variables.screen_width, variables.screen_height * (9/11))
    background_rect3 = pygame.rect.Rect(0, variables.screen_height * (2/11), variables.screen_width, variables.screen_height * (7/11))
    background_rect4 = pygame.rect.Rect(0, variables.screen_height * (3/11), variables.screen_width, variables.screen_height * (5/11))
    background_rect5 = pygame.rect.Rect(0, variables.screen_height * (4/11), variables.screen_width, variables.screen_height * (3/11))
    background_rect6 = pygame.rect.Rect(0, variables.screen_height * (5/11), variables.screen_width, variables.screen_height * (1/11))

def draw():
    pygame.draw.rect(variables.screen, background_color1, background_rect1)
    pygame.draw.rect(variables.screen, background_color2, background_rect2)
    pygame.draw.rect(variables.screen, background_color3, background_rect3)
    pygame.draw.rect(variables.screen, background_color4, background_rect4)
    pygame.draw.rect(variables.screen, background_color5, background_rect5)
    pygame.draw.rect(variables.screen, background_color6, background_rect6)