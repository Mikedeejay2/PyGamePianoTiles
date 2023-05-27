import pygame
import random
import sys
import variables

word_color = "white"
missed_color = "red"

# Set fonts
font_size = 32
font = pygame.font.Font(None, font_size)

score = 0
missed = 0
word_speed = 1
word_frequency = 150
game_over = False
game_over_display_time = 180
game_over_cur_time = 0

# Set lane positions
lane_count = 4
lane_width = variables.screen_width // lane_count
lanes = [i * lane_width + lane_width // 2 for i in range(lane_count)]

# Function to create a new word
def new_word():
    word = random.choice(variables.word_list)
    lane = random.choice(lanes)
    x = lane - font_size // 2
    y = -font_size
    return {"text": word, "x": x, "y": y, "lane": lane}

# Function to check if two words overlap
def check_overlap(word1, word2):
    rect1 = pygame.Rect(word1["x"], word1["y"], font_size * len(word1["text"]), font_size)
    rect2 = pygame.Rect(word2["x"], word2["y"], font_size * len(word2["text"]), font_size)
    return rect1.colliderect(rect2)

# Create initial word
active_words = []
new_word_count = variables.screen_height // word_frequency

# Add the first word
word = new_word()
active_words.append(word)
word_added_time = pygame.time.get_ticks()

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
                distance = abs(variables.screen_height - (word["y"] + font_size))
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
    global word_speed, score, missed, game_over, word_added_time

    # Update word positions
    for word in active_words:
        word["y"] += word_speed

    # Create new words
    time_since_word_added = pygame.time.get_ticks() - word_added_time
    if len(active_words) < new_word_count and time_since_word_added > 1000:  # Pause of 1 second
        word = new_word()

        # Check for overlap with existing words
        while any(check_overlap(word, active_word) for active_word in active_words):
            word = new_word()

        active_words.append(word)
        word_added_time = pygame.time.get_ticks()

    # Increase word speed as the game progresses
    word_speed = 1 + score // 10

    # Draw active words
    for word in active_words:
        word_surface = font.render(word["text"], True, word_color)
        variables.screen.blit(word_surface, (word["x"], word["y"]))

    # Draw score and missed counts
    score_surface = font.render(f"Score: {score}", True, word_color)
    missed_surface = font.render(f"Missed: {missed}", True, missed_color)
    variables.screen.blit(score_surface, (10, 10))
    variables.screen.blit(missed_surface, (variables.screen_width - missed_surface.get_width() - 10, 10))

    # Update the display
    pygame.display.flip()

    # Check if any words reached the bottom
    for word in active_words:
        if word["y"] >= variables.screen_height:
            active_words.remove(word)
            missed += 1
            if missed >= 3:
                game_over = True
                break

def draw_game_over():
    global word_speed, score, missed, game_over, word_added_time, game_over_cur_time
    # Game over screen
    game_over_surface = font.render("Game Over", True, word_color)
    final_score_surface = font.render(f"Final Score: {score}", True, word_color)
    variables.screen.blit(game_over_surface, (variables.screen_width // 2 - game_over_surface.get_width() // 2, variables.screen_height // 2 - font_size))
    variables.screen.blit(final_score_surface, (variables.screen_width // 2 - final_score_surface.get_width() // 2, variables.screen_height // 2 + font_size))
    game_over_cur_time += 1

    if game_over_cur_time >= game_over_display_time:
        variables.scene = "menu"
        score = 0
        missed = 0
        word_speed = 1
        game_over = False

def draw():
    if game_over:
        draw_game_over()
    else:
        draw_game()
