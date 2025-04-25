# \view.py

import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_background(screen, width, height):
    screen.fill(BLACK)

def draw_timer(screen, timer, width, height):
    font = pygame.font.Font(None, 74)
    minutes = timer // 60
    seconds = timer % 60
    time_text = font.render(f"{minutes:02d}:{seconds:02d}", True, WHITE)
    screen.blit(time_text, (width // 2 - 50, height // 2 - 50))

def draw_subject(screen, subject, width, height):
    font = pygame.font.Font(None, 36)
    subject_text = font.render(f"Studying: {subject}", True, WHITE)
    screen.blit(subject_text, (width // 2 - subject_text.get_width() // 2, height // 2 - 100))