from turtle import Turtle
from random import choice, randint


class CarManager():
    def __init__(self):
        """Init function for Car class"""
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
        self.cars =[]
        self.create_or_wait = 0
        self.car_speed = 0.1
        self.number_of_cars = 300 #lower = more cars


    def create_cars(self, screen_height, screen_width):
        """This function create a car"""
        self.create_or_wait += 1
        if self.create_or_wait % self.number_of_cars == 0:
            car_y_pos = randint(1, round((screen_height/2) * 0.90)//20)
            car_y_pos = car_y_pos * 20
            polarisation = randint(0, 1)
            if polarisation == 0:
                car_y_pos = -car_y_pos
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=2, stretch_len=4)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(choice(self.colors))
            new_car.goto(x = ((screen_width//2) + 20), y = car_y_pos)
            self.cars.append(new_car)

    def move_cars(self):
        """This function moves cars"""
        for car in self.cars:
            car.right_cor = car.xcor() + 80
            car.left_cor = car.xcor() - 80
            car.up_cor = car.ycor() + 40
            car.down_cor = car.ycor() - 40
            car.forward(self.car_speed)

    def new_level_parameters(self):
        self.number_of_cars = self.number_of_cars //2
        self.car_speed = self.car_speed * 3

    def get_edges(self, car):
        """This function calculates the edges of a car"""
        left = car.xcor() - 40
        right = car.xcor() + 40
        top = car.ycor() + 20
        bottom = car.ycor() - 20
        return left, right, top, bottom