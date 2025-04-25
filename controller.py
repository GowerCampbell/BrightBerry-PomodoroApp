# \controller.py
import pygame
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open_by_key("1oLYb0idLBhC-o48vf7PVoORmefE-CWllgna61b4pphQ").sheet1

def ensure_sheet_headers():
# Ensure the sheet has the correct headers
    headers = ["Subject", "Date", "Duration (seconds)", "Next Review"]
    if SHEET.row_values(1) != headers:
        SHEET.append_row(headers)

def log_session(subject, duration):
    ensure_sheet_headers()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    interval_days = schedule_review(subject, 1)  # Initial interval
    next_review = (datetime.now() + timedelta(days=interval_days)).strftime("%Y-%m-%d")
    SHEET.append_row([subject, date, str(duration), next_review])
    print(f"Logged to Google Sheets: Studied {subject} for {duration} seconds")

def schedule_review(subject, interval_days):
    # Basic spaced repetition logic
    ensure_sheet_headers()
    rows = SHEET.get_all_values()[1:]  # Skip header row
    
    # Find the latest entry for this subject
    latest_interval = interval_days
    for row in rows:
        if row[0] == subject:
            latest_interval = max(latest_interval, 1)  # Placeholder for interval calculation
    
    # Double the interval for the next review (simplified spaced repetition)
    new_interval = latest_interval * 2
    print(f"Scheduling review for {subject} in {new_interval} days")
    return new_interval

def handle_input(event, paused, running):
    if event.type == pygame.QUIT:
        return paused, False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:  # Space to pause/resume
            paused = not paused
        if event.key == pygame.K_r:  # 'R' to reset
            return False, True
    return paused, running