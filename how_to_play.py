import pygame
import variables
import background
import utils

text_color = "white"

font_regular = None
font_title = None

animation_frames = 15

def set_elements():
    global font_regular, font_title
    font_size = variables.screen_width // 32
    font_size_bold = variables.screen_width // 20
    font_regular = pygame.font.Font("fonts/Montserrat-Regular.ttf", font_size)
    font_title = pygame.font.Font("fonts/Montserrat-Bold.ttf", font_size_bold)

    global title_surface, title_rect
    title_surface = font_title.render("How To Play", True, text_color)
    title_rect = utils.get_rect(title_surface, 50, 10)

    global back_surface, back_rect
    back_surface = font_title.render("Back", True, text_color)
    back_rect = utils.get_rect(back_surface, 30, 80)

    global play_surface, play_rect
    play_surface = font_title.render("Play", True, text_color)
    play_rect = utils.get_rect(play_surface, 70, 80)

    global text1_surface, text1_rect
    text1_surface = font_regular.render("Tiles will fall from the top of the screen.", True, text_color)
    text1_rect = utils.get_rect(text1_surface, 50, 25)

    global text2_surface, text2_rect
    text2_surface = font_regular.render("You must stop them from reaching the bottom of the screen.", True, text_color)
    text2_rect = utils.get_rect(text2_surface, 50, 35)

    global text3_surface, text3_rect
    text3_surface = font_regular.render("Type the lower most word to make it disappear.", True, text_color)
    text3_rect = utils.get_rect(text3_surface, 50, 45)

    global text4_surface, text4_rect
    text4_surface = font_regular.render("If too many tiles reach the bottom, you lose.", True, text_color)
    text4_rect = utils.get_rect(text4_surface, 50, 55)

    global text5_surface, text5_rect
    text5_surface = font_regular.render("Have fun!", True, text_color)
    text5_rect = utils.get_rect(text5_surface, 50, 65)

def on_event(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            variables.scene = "menu"
        elif play_rect.collidepoint(mouse_pos):
            variables.scene = "game"

def draw():
    background.draw()
    variables.screen.blit(title_surface, title_rect)

    variables.screen.blit(text1_surface, text1_rect)
    variables.screen.blit(text2_surface, text2_rect)
    variables.screen.blit(text3_surface, text3_rect)
    variables.screen.blit(text4_surface, text4_rect)
    variables.screen.blit(text5_surface, text5_rect)

    variables.screen.blit(back_surface, back_rect)
    variables.screen.blit(play_surface, play_rect)
    draw_animation()

def draw_animation():
    mouse_pos = pygame.mouse.get_pos()
    rect = None
    if back_rect.collidepoint(mouse_pos):
        rect = back_rect
    elif play_rect.collidepoint(mouse_pos):
        rect = play_rect
    
    utils.animate_underline(rect, animation_frames, text_color, variables.screen_width // 500)