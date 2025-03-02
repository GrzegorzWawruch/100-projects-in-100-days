from turtle import Screen
import time


def screen_create():
    """This function create a screen"""
    screen = Screen()
    screen.setup(width=1600, height=800)
    screen.bgcolor('black')
    screen.title("Arcade game")
    screen.tracer(0)
    return screen

def screen_update(screen):
    """This function updates the screen"""
    screen.update()
    time.sleep(0.1)

def screen_key_detection(up, down, w, s, screen):
    """This function detects the keys pressed"""
    screen.listen()
    screen.onkeypress(up, "Up")
    screen.onkeypress(down, "Down")
    screen.onkeypress(s, 's')
    screen.onkeypress(w, 'w')