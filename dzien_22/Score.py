from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')

    def write_score(self, height, paddle):
        """This function will write the score to the screen."""
        self.clear()
        if paddle == "left":
            self.goto(x = -50, y = ((height/2)-((height/2)*0.2)))
        elif paddle == "right":
            self.goto(x = 50, y = ((height/2)-((height/2)*0.2)))
        self.write(f'{self.score}', False, align='center', font=('Arial', 24, 'bold'))

    def add_points(self):
        """This function will add points to the score."""
        self.score += 1
