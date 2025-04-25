# \main.py

import pygame
import sys
from time_layout import main_with_subject

# Initialize Pygame
pygame.init()

# Prompt for subject
print("Enter the subject you want to study (or press Enter to use 'General'):")
subject = input().strip() or "General"

# Run the app with the selected subject
if __name__ == "__main__":
    main_with_subject(subject)
    pygame.quit()
    sys.exit()