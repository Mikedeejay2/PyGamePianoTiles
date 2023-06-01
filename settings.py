import variables
import pygame
import utils

text_color = "white"
title_font = None
setting_font = None

title_surf = None
title_rect = None

back_surf = None
back_rect = None

setting_color = "cadetblue3"
setting_outline_color = "cadetblue2"

resolution_rect = None
fullscreen_rect = None

resolution_index = 3 # 1280, 720

def set_elements():
    global title_font, setting_font, title_surf, title_rect, settings, back_surf, back_rect
    title_font = pygame.font.Font(None, variables.screen_width // 15)
    setting_font = pygame.font.Font(None, variables.screen_width // 30)
    title_surf = title_font.render("Settings", True, text_color)
    title_rect = utils.get_rect(title_surf, 20, 10)
    
    back_surf = title_font.render("Back...", True, text_color)
    back_rect = utils.get_rect(back_surf, 20, 80)

    global resolution_rect, fullscreen_rect
    padding = variables.screen_width // 10
    resolution_rect = pygame.rect.Rect(padding, variables.screen_height * 0.2, variables.screen_width - padding * 2, variables.screen_height * 0.2)
    fullscreen_rect = pygame.rect.Rect(padding, variables.screen_height * 0.5, variables.screen_width - padding * 2, variables.screen_height * 0.2)

def draw():
    variables.screen.blit(title_surf, title_rect)
    mouse_pos = pygame.mouse.get_pos()

    variables.screen.blit(back_surf, back_rect)
    if back_rect.collidepoint(mouse_pos):
        utils.animate_underline(back_rect, 15, text_color, variables.screen_width // 500)
    else:
        utils.animate_underline(None, 0, None, None) # Reset animation

    pygame.draw.rect(variables.screen, setting_color, resolution_rect, 0, 10)
    if resolution_rect.collidepoint(mouse_pos):
        pygame.draw.rect(variables.screen, text_color, resolution_rect, 10, 10)
    else:
        pygame.draw.rect(variables.screen, setting_outline_color, resolution_rect, 10, 10)
    resolution_text = setting_font.render("Current resolution: " + str(variables.screen_width) + ", " + str(variables.screen_height), True, text_color)
    resolution_text_rect = utils.get_rect(resolution_text, 50, 30)
    variables.screen.blit(resolution_text, resolution_text_rect)

    pygame.draw.rect(variables.screen, setting_color, fullscreen_rect, 0, 10)
    if fullscreen_rect.collidepoint(mouse_pos):
        pygame.draw.rect(variables.screen, text_color, fullscreen_rect, 10, 10)
    else:
        pygame.draw.rect(variables.screen, setting_outline_color, fullscreen_rect, 10, 10)
    
    fullscreen_text = None
    if variables.fullscreen:
        fullscreen_text = setting_font.render("Exit Fullscreen", True, text_color)
    else:
        fullscreen_text = setting_font.render("Enter Fullscreen", True, text_color)
    fullscreen_text_rect = utils.get_rect(fullscreen_text, 50, 60)
    variables.screen.blit(fullscreen_text, fullscreen_text_rect)

def on_event(event: pygame.event.Event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            variables.scene = "menu"
        elif resolution_rect.collidepoint(mouse_pos):
            if variables.fullscreen:
                variables.toggle_fullscreen()
            global resolution_index
            resolution_index += 1
            new_res = variables.supported_resolutions[resolution_index]
            if new_res[0] > variables.monitor_width or new_res[1] > variables.monitor_height or resolution_index >= len(variables.supported_resolutions):
                resolution_index = 0
                new_res = variables.supported_resolutions[0]
            variables.set_res(new_res[0], new_res[1])
            print("Changed resolution to " + str(new_res))
        elif fullscreen_rect.collidepoint(mouse_pos):
            variables.set_res(variables.monitor_width, variables.monitor_height)
            variables.toggle_fullscreen()
            if not variables.fullscreen:
                new_res = variables.supported_resolutions[resolution_index]
                variables.set_res(new_res[0], new_res[1])