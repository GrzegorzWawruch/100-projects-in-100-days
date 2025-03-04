from turtle import Screen
import time


def create_screen():
    """This function creates a new Screen"""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0) #its turn off the animations
    return screen

def screen_update(screen):
    """This function updates the screen"""
    screen.update()
    time.sleep(0.1)

def exit_from_the_screen(screen):
    """This function exits when we use mouse click"""
    screen.exitonclick()

def key_detection(left, right, up, down, screen):
    """This function detects keys, which are pressed by user"""
    screen.listen()
    screen.onkeypress(left, 'Left')
    screen.onkeypress(right, 'Right')
    screen.onkeypress(up, 'Up')
    screen.onkeypress(down, 'Down')