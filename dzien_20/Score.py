from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.setposition(x=0, y=270)
        self.write(f'Score: {self.score}',False , align='center', font=('Arial', 16, 'bold'))

    def add_points(self):
        self.clear()
        self.score += 1
        self.setposition(x=0, y=270)
        self.write(f'Score: {self.score}', False, align='center', font=('Arial', 16, 'bold'))
        self.paint_upper_border()

    def end_game(self):
        self.setposition(0,0)
        self.color("red")
        self.write(f'GAME OVER', False, align='center', font=('Arial', 16, 'bold'))

    def paint_upper_border(self):
        self.goto(x=-300, y=260)
        self.color('yellow')
        self.showturtle()
        self.pendown()
        self.forward(600)
        self.hideturtle()
        self.penup()

