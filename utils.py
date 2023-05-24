import pygame
import variables

underline_current_frame = 0

# Used to place a surface to the screen in relation to the size of the screen for resizable elements
def get_rect(surface, percent_width, percent_height):
    return surface.get_rect(center = (
        variables.screen_width * (percent_width / 100), 
        variables.screen_height * (percent_height / 100)
        ))

def animate_underline(rect, total_frames, color, width):
    global underline_current_frame
    if rect is not None:
        start_pos = rect.bottomleft
        end_pos = rect.bottomright
        # Get the distance between the start and the end
        distance = end_pos[0] - start_pos[0]
        # Get the current percent through the animation
        distance_percent = underline_current_frame / total_frames
        # Get the ending position of this frame of animation
        cur_pos = (start_pos[0] + (distance * distance_percent), end_pos[1])
        # Increment frame if there in animation
        if underline_current_frame < total_frames:
            underline_current_frame += 1
        
        pygame.draw.line(variables.screen, color, start_pos, cur_pos, int(width))
    else:
        underline_current_frame = 0