from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        """ Init function for Score class"""
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('black')

    def write_score(self, height, width):
        """This function display score on the left top corner"""
        self.clear()
        xcor = - round((height/2)*0.95)
        ycor = round(width/2 - width * 0.06)
        self.pendown()
        self.showturtle()
        self.setpos(x = xcor, y = ycor )
        self.write(f'Score: {self.score}',move=False , align='center', font=('Arial', 16, 'bold'))
        self.hideturtle()
        self.penup()

    def write_end_game(self):
        """This function display end game writing """
        self.penup()
        self.hideturtle()
        self.setpos(x = 0, y = 0)
        self.write(f'GAME OVER', move=False , align='center', font=('Arial', 32, 'bold'))

    def add_score(self):
        """This function add point to score"""
        self.score += 1