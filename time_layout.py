# \time_layout.py
import pygame
import time
from controller import handle_input, log_session, schedule_review
from view import draw_background, draw_timer, draw_subject
from animations import animate_flower

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Blueberry Timer")

# Timer settings
POMODORO_TIME = 25 * 60  # 25 minutes in seconds
timer = POMODORO_TIME
running = True
start_time = None
paused = False

def setup():
    global start_time
    start_time = time.time()

def main_with_subject(subject):
    global timer, running, paused, start_time
    setup()
    while running:
        for event in pygame.event.get():
            paused, running = handle_input(event, paused, running)

        if not paused and running:
            elapsed = time.time() - start_time
            timer = max(0, POMODORO_TIME - int(elapsed))
        else:
            start_time = time.time() - (POMODORO_TIME - timer)

        # Render using view.py
        draw_background(screen, WIDTH, HEIGHT)
        draw_subject(screen, subject, WIDTH, HEIGHT)
        draw_timer(screen, timer, WIDTH, HEIGHT)
        
        # Draw animated flower
        timer_progress = 1 - (timer / POMODORO_TIME)  # 0 to 1 as timer decreases
        flower_y = HEIGHT - 100 - (POMODORO_TIME - timer) // 10
        animate_flower(screen, WIDTH // 2 - 15, flower_y, timer_progress)

        # If timer reaches 0, log session and reset
        if timer <= 0 and running:
            log_session(subject, POMODORO_TIME)
            schedule_review(subject, 1)
            setup()

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # 60 FPS

if __name__ == "__main__":
    main_with_subject("General")