import pygame
import random
import sys
import variables
import background
import math

word_color = "black"
missed_color = "red"
note_color = "white"
note_outline_color = "cadetblue2"

# Set fonts
font_unselected = None
font_selected = None

score = 0
missed = 0
word_speed = 1.0
word_frequency = 150
game_over = False
game_over_display_time = 180
game_over_cur_time = 0
time_until_next_word = 0

# Set lane positions
lane_count = 4
lane_width = 0
lanes = None
new_word_count = 0
note_size = 0

# Create initial word
active_words = []

# Add the first word
word_added_time = pygame.time.get_ticks()

def set_elements():
    global lane_width, lanes, new_word_count, note_size, font_unselected, font_selected, font_unselected
    font_size = variables.screen_width // 40
    font_size_selected = variables.screen_width // 37
    font_selected = pygame.font.Font("fonts/Montserrat-Bold.ttf", font_size_selected)
    font_unselected = pygame.font.Font("fonts/Montserrat-Regular.ttf", font_size)
    lane_width = variables.screen_width // lane_count // 1.4
    note_size = lane_width
    lanes = [i * lane_width + variables.screen_width * 0.14 for i in range(lane_count)]
    new_word_count = variables.screen_height // word_frequency

# Function to create a new word
def new_word():
    word = random.choice(variables.word_list)
    lane = random.choice(lanes)
    rect = pygame.rect.Rect(lane, -note_size, note_size, note_size)
    return {"text": word, "rect": rect, "y": float(rect.y)}

# Function to check if two words overlap
def check_overlap(word1, word2):
    return word1["rect"].colliderect(word2["rect"])

def on_event(event):
    global game_over, score, missed
    if event.type == pygame.QUIT:
            game_over = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game_over = True
        else:
            # Find the closest word to the bottom
            closest_word = None
            closest_distance = sys.maxsize
            for word in active_words:
                rect = word["rect"]
                distance = abs(variables.screen_height - rect.y)
                if distance < closest_distance:
                    closest_word = word
                    closest_distance = distance

            # Check if typed key matches the closest word
            if closest_word and closest_word["text"].startswith(pygame.key.name(event.key)):
                closest_word["text"] = closest_word["text"][1:]
                if not closest_word["text"]:
                    active_words.remove(closest_word)
                    score += 1
            else:
                missed += 1

def draw_game():
    global word_speed, score, missed, game_over, word_added_time, time_until_next_word

    # Update word positions
    for word in active_words:
        word["y"] += word_speed

    # Create new words
    time_since_word_added = pygame.time.get_ticks() - word_added_time
    if len(active_words) < new_word_count and time_since_word_added > time_until_next_word or len(active_words) == 0:  # Pause of 1 second
        try_place_new_word()

    # Increase word speed as the game progresses
    word_speed = (1.2 + math.sqrt(score) / 5) * (variables.screen_height / 720)
    time_until_next_word = (2000 - math.sqrt(score) * 200) * (variables.screen_height / 720)

    outline_size = variables.screen_width // 200
    # Draw active words
    for word in active_words:
        rect = word["rect"]
        rect.y = word["y"]
        pygame.draw.rect(variables.screen, note_color, rect, 0, outline_size)
        word_surface = None
        if word == active_words[0]:
            cur_color = (max((rect.y - variables.screen_height / 3) / variables.screen_height * 300, 0), 0, 0)
            pygame.draw.rect(variables.screen, cur_color, rect, outline_size, outline_size)
            word_surface = font_selected.render(word["text"], True, cur_color)
        else:
            pygame.draw.rect(variables.screen, note_outline_color, rect, outline_size, outline_size)
            word_surface = font_unselected.render(word["text"], True, word_color)
        word_x = rect.x + (rect.width - word_surface.get_width()) // 2
        word_y = rect.y + (rect.height - word_surface.get_height()) // 2
        variables.screen.blit(word_surface, (word_x, word_y))
    
    for lane in lanes:
        pygame.draw.line(variables.screen, "black", (lane, 0), (lane, variables.screen_height), variables.screen_width // 400)
    pygame.draw.line(variables.screen, "black", (lanes[-1] + note_size, 0), (lanes[-1] + note_size, variables.screen_height), variables.screen_width // 400)

    # Draw score and missed counts
    score_surface = font_selected.render(f"Score: {score}", True, word_color)
    missed_surface = font_selected.render(f"Missed: {missed}", True, missed_color)
    variables.screen.blit(score_surface, (10, 10))
    variables.screen.blit(missed_surface, (variables.screen_width - missed_surface.get_width() - 10, 10))

    # Check if any words reached the bottom
    for word in active_words:
        rect = word["rect"]
        if rect.y >= variables.screen_height:
            active_words.remove(word)
            missed += 1
            if missed >= 3:
                game_over = True
                break

def draw_game_over():
    global word_speed, score, missed, game_over, word_added_time, game_over_cur_time, time_until_next_word
    # Game over screen
    game_over_surface = font_selected.render("Game Over", True, word_color)
    final_score_surface = font_selected.render(f"Final Score: {score}", True, word_color)
    final_missed_surface = font_selected.render(f"Missed: {missed}", True, missed_color)
    variables.screen.blit(game_over_surface, (variables.screen_width // 2 - game_over_surface.get_width() // 2, variables.screen_height * 0.3))
    variables.screen.blit(final_score_surface, (variables.screen_width // 2 - final_score_surface.get_width() // 2, variables.screen_height * 0.45))
    variables.screen.blit(final_missed_surface, (variables.screen_width // 2 - final_missed_surface.get_width() // 2, variables.screen_height * 0.6))
    game_over_cur_time += 1

    if game_over_cur_time >= game_over_display_time:
        variables.scene = "menu"
        score = 0
        missed = 0
        word_speed = 1
        game_over = False
        active_words.clear()
        game_over_cur_time = 0
        time_until_next_word = 0

def draw():
    background.draw()
    if game_over:
        draw_game_over()
    else:
        draw_game()

def try_place_new_word():
    global word_added_time
    word = new_word()

    # Check for overlap with existing words
    place = True
    for active_word in active_words:
        if check_overlap(active_word, word):
            place = False
    
    if place:
        active_words.append(word)
        word_added_time = pygame.time.get_ticks()