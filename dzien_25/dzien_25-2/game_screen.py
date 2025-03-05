import turtle
from turtle import Screen, Turtle

my_screen = Screen()

def create_screen(my_screen):
    """This function creates screen"""
    my_screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    my_screen.addshape(image)
    turtle.shape(image)

def exit_on_click(my_screen):
    """This function allow us to exit from screen window by click on it"""
    my_screen.exitonclick()

def get_mouse_click_coor(x, y):
    """This function allow us to print x and y coordinates"""
    print(x, y)

def on_screen_click():
    """This function allow us to use get_mouse_click function on turtle"""
    turtle.onclick(get_mouse_click_coor)

def write_state_name_on_map(state_name, x, y):
    answer_turtle = Turtle()
    answer_turtle.penup()
    answer_turtle.hideturtle()
    answer_turtle.goto(x, y)
    answer_turtle.write(state_name, align="center", font=("Arial", 12, "bold"))