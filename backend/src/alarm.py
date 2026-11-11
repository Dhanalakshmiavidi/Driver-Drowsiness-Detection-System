"""import pygame

pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load("backend\src\mixkit-alert-alarm-1005.wav")
    pygame.mixer.music.play()"""

import winsound

def play_alarm(level):
    if level == "low":
        winsound.Beep(1000, 200)

    elif level == "medium":
        winsound.Beep(1500, 500)

    elif level == "high":
        winsound.Beep(2000, 1000)