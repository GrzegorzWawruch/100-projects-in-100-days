from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        """This function define player create"""
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.speed('fastest')
        self.setheading(90)  # facing up initially
        self.size = 20  # set size of the player (the half size of player)
        self.update_corners()

    def update_corners(self):
        """Update the corners of the player after every move"""
        half_size = self.size
        if self.heading() == 90:  # move up
            self.right_cor = self.xcor() + half_size
            self.left_cor = self.xcor() - half_size
            self.up_cor = self.ycor() + half_size
            self.down_cor = self.ycor() - half_size
        elif self.heading() == 180:  # move left
            self.up_cor = self.xcor() - half_size
            self.down_cor = self.xcor() + half_size
            self.right_cor = self.ycor() + half_size
            self.left_cor = self.ycor() - half_size
        elif self.heading() == 0:  # move right
            self.up_cor = self.xcor() + half_size
            self.down_cor = self.xcor() - half_size
            self.left_cor = self.ycor() + half_size
            self.right_cor = self.ycor() - half_size

    def set_start_player_position(self, height):
        """This function move player to start position"""
        y = (-(height / 2)) + (height * 0.1)
        self.goto(x=0, y=y)
        self.update_corners()

    def move_up(self):
        """This function define how player move"""
        self.setheading(90)
        self.forward(30)
        self.update_corners()

    def move_left(self):
        """This function define how player move"""
        self.setheading(180)
        self.forward(30)
        self.update_corners()

    def move_right(self):
        """This function define how player move"""
        self.setheading(0)
        self.forward(30)
        self.update_corners()

    def get_edges(self):
        """Returns the current edges of the player"""
        return self.left_cor, self.right_cor, self.up_cor, self.down_cor
