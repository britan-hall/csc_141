import pygame as py

def draw_star_bg(screen, bg_images, scroll_positions, scroll_speeds, frame_height):
    """
    Draws a parallax scrolling background with multiple layers of stars.
    """
    for i, bg in enumerate(bg_images):
        # Scroll position for this layer
        scroll_positions[i] += scroll_speeds[i]
        scroll_positions[i] %= frame_height  

        # Draw the current layer twice
        screen.blit(bg, (0, -frame_height + scroll_positions[i]))
        screen.blit(bg, (0, scroll_positions[i]))
