
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
x = 0


for turtle_index in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtles.append(turtle)


for i in range(-100, 140, 40):
    turtles[x].goto(x = -230, y = i)
    x +=1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        z = random.randint(5,25)
        turtle.forward(z)
        if turtle.xcor() > 220:
            if user_bet == turtle.pencolor():
                print(f'You\'ve won! The {turtle.pencolor()} is the winner! ')
                is_race_on = False
            else:
                print(f'You\'ve lost! The {turtle.pencolor()} is the winner! ')
                is_race_on = False

screen.exitonclick()