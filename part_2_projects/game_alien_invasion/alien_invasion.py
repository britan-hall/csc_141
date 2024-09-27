import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
import json

# Filepath for high scores
high_scores_file = 'high_scores.json'

title_image = pygame.image.load('images\cover.jpg')

# Function to load high scores from a JSON file
def load_high_scores():
    """Loads high scores from a file, returns an empty list if the file doesn't exist or is invalid."""
    try:
        with open(high_scores_file, 'r') as f:
            data = f.read().strip()  # Strip any leading/trailing spaces or newlines
            if not data:
                return []  # If file is empty, return an empty list
            return json.loads(data)  # Parse the JSON data
    except FileNotFoundError:
        return []  # If no file, return an empty list
    except json.JSONDecodeError:
        return []  # If file is invalid, return an empty list

# Function to save high scores to a JSON file
def save_high_scores(high_scores):
    """Saves high scores to a file."""
    with open(high_scores_file, 'w') as f:
        json.dump(high_scores, f, indent=4)

# Function to update the high scores if the current score qualifies
def update_high_scores(name, score):
    """Updates the high score list if the current score is in the top 3."""
    # Load existing high scores
    high_scores = load_high_scores()

    # Append new score
    high_scores.append({'name': name, 'score': score})

    # Sort scores in descending order by score
    high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)

    # Keep only the top 5 scores, can be changed
    high_scores = high_scores[:5]

    # Save the updated high scores
    save_high_scores(high_scores)

# Function to render text on the screen
def render_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Load the title image
    title_image = pygame.image.load('images\cover.jpg')

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    player_name = ""  # Initialize player_name as an empty string
    asking_for_name = True  # Start by asking for the player's name
    input_active = True  # Track whether name input is active
    
    font = pygame.font.SysFont(None, 48)  # Font for text input
    small_font = pygame.font.SysFont(None, 36)  # Font for displaying high scores

    while True:
        screen.fill(ai_settings.bg_color)  # Fill the screen with background color

        # Handle input for player's name
        if asking_for_name:
            render_text(screen, "Enter Your Name:", font, (255, 255, 255), 100, 100)
            render_text(screen, player_name, font, (255, 255, 255), 100, 160)

            # Load and display high scores
            high_scores = load_high_scores()
            if high_scores:
                render_text(screen, "Top Scores:", small_font, (255, 255, 255), 100, 220)
                for idx, score_entry in enumerate(high_scores):
                    name = score_entry['name']
                    score = score_entry['score']
                    render_text(screen, f"{idx + 1}. {name}: {score}", small_font, (255, 255, 255), 100, 260 + idx * 40)

            # Render the title image on the right side of the screen
            title_x = 450
            title_y = 0
            screen.blit(title_image, (title_x, title_y))

            # Event handling for text input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and player_name != "":
                        asking_for_name = False  # Name entered, stop asking
                        input_active = False  # Disable input mode
                        stats.reset_stats()  # Reset game statistics for the new round
                        stats.game_active = True  # Start the game
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Remove last character
                    else:
                        # Add characters to the player name (limit to 10 characters)
                        if len(player_name) < 10:
                            player_name += event.unicode

        if stats.game_active and not asking_for_name:
            # Game logic here after player name is entered
            gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
                            aliens, bullets)
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                              aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # Displaying the gameplay
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
                             bullets, play_button)
        else:
            # Game has ended, update high scores with final score if player_name is set
            if player_name and not asking_for_name and not stats.game_active:
                final_score = stats.score  # Assuming stats.score tracks the final score
                update_high_scores(player_name, final_score)
                
                # Reset for new game
                player_name = ""  # Clear player name
                asking_for_name = True  # Ask for a new name
                stats.game_active = False  # Ensure game does not restart without name input

        pygame.display.flip()  # Update the display

run_game()