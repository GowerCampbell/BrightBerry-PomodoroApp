# \animations.py
import pygame
import math
import os

# Path to assets
ASSETS_PATH = "assets"
BLUEBERRY_FLOWER_IMAGE = os.path.join(ASSETS_PATH, "blueberry_flower.png")

# Load the blueberry flower image
try:
    blueberry_flower = pygame.image.load(BLUEBERRY_FLOWER_IMAGE).convert_alpha()
    # Scale the image to a reasonable size (e.g., 50x50 pixels)
    blueberry_flower = pygame.transform.scale(blueberry_flower, (50, 50))
except pygame.error as e:
    print(f"Error loading blueberry_flower.png: {e}")
    # Fallback to a simple shape if the image fails to load
    blueberry_flower = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.circle(blueberry_flower, (90, 50, 150), (25, 25), 20)

def animate_flower(screen, x, y, timer_progress):
    # Pulsing effect
    pulse_scale = 1 + 0.1 * math.sin(pygame.time.get_ticks() * 0.005)
    scaled_size = (int(50 * pulse_scale), int(50 * pulse_scale))
    scaled_flower = pygame.transform.scale(blueberry_flower, scaled_size)

    # Adjust position to center the image
    flower_rect = scaled_flower.get_rect(center=(x + 25, y - int(timer_progress * 20)))
    screen.blit(scaled_flower, flower_rect)