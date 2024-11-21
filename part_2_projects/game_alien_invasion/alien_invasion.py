import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import high_score
import game_functions as gf
from stars import draw_star_bg

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

    bg_images = [
        pygame.transform.scale(pygame.image.load("images/background/background_1.png").convert(), (ai_settings.screen_width, ai_settings.screen_height)),
        pygame.transform.scale(pygame.image.load("images/background/background_2.png").convert(), (ai_settings.screen_width, ai_settings.screen_height)),
        pygame.transform.scale(pygame.image.load("images/background/background_3.png").convert(), (ai_settings.screen_width, ai_settings.screen_height)),
        pygame.transform.scale(pygame.image.load("images/background/background_4.png").convert(), (ai_settings.screen_width, ai_settings.screen_height)),
    ]

    # Initialize scroll positions and speeds
    scroll_positions = [0, 0, 0, 0]
    scroll_speeds = [.1, .4, .3, .2]

    # Load the title image
    title_image = pygame.image.load('images/cover.jpg')

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
    
    player_name = ""
    asking_for_name = True
    input_active = True
    
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 36)

    while True:
        screen.fill(ai_settings.bg_color)

        if asking_for_name:
            render_text(screen, "Enter Your Name:", font, (255, 255, 255), 100, 100)
            render_text(screen, player_name, font, (255, 255, 255), 100, 160)

            high_scores = high_score.load_high_scores()
            if high_scores:
                render_text(screen, "Top Scores:", small_font, (255, 255, 255), 100, 220)
                for idx, score_entry in enumerate(high_scores):
                    name = score_entry['name']
                    score = score_entry['score']
                    render_text(screen, f"{idx + 1}. {name}: {score}", small_font, (255, 255, 255), 100, 260 + idx * 40)

            title_x = 450
            title_y = 0
            screen.blit(title_image, (title_x, title_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and player_name != "":
                        asking_for_name = False
                        input_active = False
                        stats.reset_stats()
                        stats.game_active = True
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        if len(player_name) < 10:
                            player_name += event.unicode

        if stats.game_active and not asking_for_name:
            # Draw the parallax stars
            draw_star_bg(screen, bg_images, scroll_positions, scroll_speeds, ai_settings.screen_height)

            # Game logic
            gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # Update screen with all elements
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        else:
            if player_name and not asking_for_name and not stats.game_active:
                final_score = stats.score
                high_score.update_high_scores(player_name, final_score)
                player_name = ""
                asking_for_name = True
                stats.game_active = False

        pygame.display.flip()

run_game()
