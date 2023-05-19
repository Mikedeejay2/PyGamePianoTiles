import pygame
from sys import exit

pygame.init()

screen_width = 1280
screen_height = 720
center_width = screen_width / 2
center_height = screen_height / 2

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Piano Tiles Game")
clock = pygame.time.Clock()
title_font = pygame.font.Font(None, 100)
button_font = pygame.font.Font(None, 40)

# https://www.webucator.com/article/python-color-constants-module/
button_color = "aliceblue"
background_color = "aqua"
button_text_color = "black"

background_surface = pygame.Surface((screen_width, screen_height))
background_surface.fill(background_color)
menu_title_surface = title_font.render("Piano Tiles", True, "White")
menu_title_rect = menu_title_surface.get_rect(center = (screen_width / 2, 150))

button_row1_y = 300
button_row1_spacing = 50
button_row1_width = 250
button_row1_height = 80

menu_button1_location = (center_width - (button_row1_spacing / 2) - (button_row1_width / 2), button_row1_y)
menu_button1_surface = pygame.Surface((button_row1_width, button_row1_height))
menu_button1_surface.fill(button_color)
menu_button1_rect = menu_button1_surface.get_rect(center = menu_button1_location)
menu_button1_text_surface = button_font.render("Settings", True, button_text_color)
menu_button1_text_rect = menu_button1_text_surface.get_rect(center = menu_button1_location)

menu_button2_location = (center_width + (button_row1_spacing / 2) + (button_row1_width / 2), button_row1_y)
menu_button2_surface = pygame.Surface((button_row1_width, button_row1_height))
menu_button2_surface.fill(button_color)
menu_button2_rect = menu_button2_surface.get_rect(center = menu_button2_location)
menu_button2_text_surface = button_font.render("Exit", True, button_text_color)
menu_button2_text_rect = menu_button2_text_surface.get_rect(center = menu_button2_location)

button_row2_y = 500
button_row2_width = 550
button_row2_height = 80

menu_button3_location = (center_width, button_row2_y)
menu_button3_surface = pygame.Surface((button_row2_width, button_row2_height))
menu_button3_surface.fill(button_color)
menu_button3_rect = menu_button3_surface.get_rect(center = menu_button3_location)
menu_button3_text_surface = button_font.render("Play", True, "Black")
menu_button3_text_rect = menu_button3_text_surface.get_rect(center = menu_button3_location)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if menu_button1_rect.collidepoint(mouse_pos):
                print("Settings button pressed")
            elif menu_button2_rect.collidepoint(mouse_pos):
                print("Exit button pressed")
                pygame.quit()
                exit()
            elif menu_button3_rect.collidepoint(mouse_pos):
                print("Play button pressed")

    
    screen.blit(background_surface, (0, 0))
    screen.blit(menu_title_surface, menu_title_rect)

    screen.blit(menu_button1_surface, menu_button1_rect)
    screen.blit(menu_button1_text_surface, menu_button1_text_rect)

    screen.blit(menu_button2_surface, menu_button2_rect)
    screen.blit(menu_button2_text_surface, menu_button2_text_rect)

    screen.blit(menu_button3_surface, menu_button3_rect)
    screen.blit(menu_button3_text_surface, menu_button3_text_rect)
    
    pygame.display.update()
    clock.tick(60)