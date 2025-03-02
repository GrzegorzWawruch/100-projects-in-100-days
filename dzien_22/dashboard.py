from turtle import Turtle

class Dashboard(Turtle):
    """Definition of dashboard class"""
    def __init__(self):
        super().__init__()
        self.pencolor('white')

    def draw_middle_line(self, screen):
        """Function which draw a middle line"""
        height = screen.window_height()
        self.penup()
        self.goto(x = 0, y = -(height/2) )
        self.setheading(90)
        self.hideturtle()

        line_length = height/32

        for i in range(0,32):
            if self.ycor() < ((height/2)-((height/2)*0.3)):
                if i%2 == 0:
                    self.pendown()
                    self.forward(line_length)

                if i%2 == 1:
                    self.penup()
                    self.forward(line_length)

    def draw_a_upper_line(self, screen):
        """Function which draw upper line"""
        height = screen.window_height()
        width = screen.window_width()
        self.penup()
        self.setheading(0)
        self.goto(x = -(width/2), y = ((height/2)-((height/2)*0.3)))
        self.pendown()
        self.forward(screen.window_width())


