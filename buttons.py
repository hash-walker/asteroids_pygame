import pygame
from constants import *

def button(screen, position_x, position_y ,button_text, button_color, button_width, button_height, font_size, font_color):

    font = pygame.font.Font(None, font_size)
    button = pygame.Rect( (SCREEN_WIDTH - button_width) / 2 + position_x,(SCREEN_HEIGHT - button_height) / 2 + position_y, button_width, button_height)
    pygame.draw.rect(screen, button_color, button)
    # Render font
    text_surface = font.render(button_text, True, font_color)
    # center the text
    text_rect = text_surface.get_rect(center = button.center)
    screen.blit(text_surface, text_rect)

    return button