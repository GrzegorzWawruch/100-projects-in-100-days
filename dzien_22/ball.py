from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('yellow')
        self.shape('circle')
        self.speed('fastest')
        self.shapesize(0.5, 0.5, 0.5)
        self.left(45)

    def move_ball(self):
        """Function to move the ball"""
        self.forward(15)

    def reset_ball(self, side):
        """Function to reset the ball"""
        self.setposition(0, 0)
        if side == 'left':
            self.setheading(45)
        elif side == 'right':
            self.setheading(135)
        self.forward(15)
