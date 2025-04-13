import pygame
import sys
from graph import *
from app import *
from constants import *

def login():
    # displays background color, title, and text for mode selection
    screen.fill(BG_COLOR)

    title_font = pygame.font.Font(None, 64)
    title_text = title_font.render("LOGIN", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("GatorGo")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # this automatically passes the screen to all functions
    login()