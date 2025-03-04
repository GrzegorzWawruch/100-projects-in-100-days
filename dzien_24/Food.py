from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.shapesize(0.5 , 0.5 , 0.5)
        self.speed("fastest")

    def move_food(self):
        self.setposition(x = (randint(-14, 14)*20), y = (randint(-14,11)*20) )