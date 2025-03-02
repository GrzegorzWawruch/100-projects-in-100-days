from turtle import Screen

my_screen = Screen()

def create_screen(screen):
    """Init function for window class"""
    screen.screensize(800, 800)
    screen.bgcolor('white')
    screen.tracer(0)
    screen.title('Cross the road game')

def screen_update(screen):
    """This function update the screen and items on it"""
    screen.update()

def exit_from_the_screen(screen):
    """This function exits when we use mouse click"""
    screen.exitonclick()

def screen_height(screen):
    """This function return window high"""
    return screen.window_height()

def screen_width(screen):
    """This function return window width"""
    return screen.window_width()

def key_detection(screen, up, left, right):
    """This function detect keys and sign them functions"""
    screen.listen()
    screen.onkeypress(up, 'Up')
    screen.onkeypress(left, 'Left')
    screen.onkeypress(right, 'Right')