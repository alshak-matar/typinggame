import pygame
import random

pygame.init()

# Setting up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Typing Game")

# Setting up the font
font = pygame.font.SysFont(None, 40)

# Setting up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Setting up the variables
word_list = ["apple", "banana", "cherry", "orange", "grape", "lemon"]
current_word = ""
input_word = ""
score = 0
time_remaining = 60
clock = pygame.time.Clock()

# Setting up the timer event
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_word = input_word[:-1]
            elif event.key == pygame.K_RETURN:
                if input_word == current_word:
                    score += 1
                input_word = ""
            else:
                input_word += event.unicode
        elif event.type == timer_event:
            time_remaining -= 1
            if time_remaining == 0:
                running = False

    # Set up the background
    screen.fill(white)

    # Generate a new word if necessary
    if not current_word:
        current_word = random.choice(word_list)

    # Display the current word
    word_surface = font.render(current_word, True, black)
    word_rect = word_surface.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(word_surface, word_rect)

    # Display the input word and score
    input_surface = font.render(input_word, True, black)
    input_rect = input_surface.get_rect(center=(screen_width/2, screen_height/2 + 50))
    screen.blit(input_surface, input_rect)

    score_surface = font.render(f"Score: {score}", True, black)
    score_rect = score_surface.get_rect(topright=(screen_width-10, 10))
    screen.blit(score_surface, score_rect)

    # Display the time remaining
    time_surface = font.render(f"Time: {time_remaining}", True, black)
    time_rect = time_surface.get_rect(topleft=(10, 10))
    screen.blit(time_surface, time_rect)

    # Update display
    pygame.display.update()

    # Check if the current word has been typed correctly
    if input_word == current_word:
        current_word = ""
        input_word = ""

    # Limit the frame rate
    clock.tick(60)

# we hove here the final score
game_over_surface = font.render(f"Game Over! Final Score: {score}", True, black)
game_over_rect = game_over_surface.get_rect(center=(screen_width/2, screen_height/2))
screen.blit(game_over_surface, game_over_rect)
pygame.display.update()

# close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
