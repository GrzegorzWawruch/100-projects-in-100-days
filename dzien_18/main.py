from turtle import Turtle, Screen
import random


screen = Screen()
screen.screensize(800, 800)
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('circle')
timmy_the_turtle.shapesize(1,1)
timmy_the_turtle.pensize(18)
timmy_the_turtle.penup()
color_list = []


for i in range(-20, 20):
    timmy_the_turtle.setposition(-400,(i*20))
    for j in range(40):
        a = random.randint(1,255)
        b = random.randint(1,255)
        c = random.randint(1,255)
        timmy_the_turtle.pencolor(a, b, c)
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(1)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(19)


screen.exitonclick()