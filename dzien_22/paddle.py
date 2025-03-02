from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)

    def set_left_paddle(self, screen):
        """This function set paddle to the left side of screen"""
        screen_width = screen.window_width()
        self.setposition(x = ((-(screen_width/2)) + 20), y = 0)

    def set_right_paddle(self, screen):
        """This function set paddle to the right side of screen"""
        screen_width = screen.window_width()
        self.setposition(x = ((screen_width/2) - 30), y = 0)

    def move_paddle_up(self):
        """This function move paddle up"""
        self.forward(10)

    def move_paddle_down(self):
        """This function move paddle down"""
        self.backward(10)
