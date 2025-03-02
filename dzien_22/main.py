from dashboard import Dashboard
from my_screen import *
from paddle import Paddle
from ball import Ball
from Score import Score

left_paddle = Paddle()
right_paddle = Paddle()
my_ball = Ball()
left_paddle_score = Score()
right_paddle_score = Score()
my_screen = screen_create()

window_width = my_screen.window_width()
window_height = my_screen.window_height()

left_paddle.set_left_paddle(my_screen)
right_paddle.set_right_paddle(my_screen)

dashboard = Dashboard()
dashboard.draw_middle_line(my_screen)
dashboard.draw_a_upper_line(my_screen)
game_is_on = True

while game_is_on:

    left_paddle_score.write_score(window_height, "left")
    right_paddle_score.write_score(window_height, "right")

    my_ball.move_ball()
    screen_key_detection(right_paddle.move_paddle_up, right_paddle.move_paddle_down, left_paddle.move_paddle_up, left_paddle.move_paddle_down, my_screen)
    screen_update(my_screen)

    #Ball collision with walls
    if my_ball.ycor() > ((window_height/2)-((window_height/2)*0.3))-10 or my_ball.ycor() < -(window_height/2) + 10:
        if my_ball.heading() == 45:
            my_ball.right(90)
        elif my_ball.heading() == 135:
            my_ball.right(270)
        elif my_ball.heading() == 225:
            my_ball.right(90)
        elif my_ball.heading() == 315:
            my_ball.right(270)

    #Ball collision with paddles
    if my_ball.distance(left_paddle) < 20:
        if my_ball.heading() == 135:
            my_ball.right(90)
        elif my_ball.heading() == 225:
            my_ball.right(270)
    elif my_ball.distance(right_paddle) < 20:
        if my_ball.heading() == 45:
            my_ball.right(270)
        elif my_ball.heading() == 315:
            my_ball.right(90)

    #Ball behind the puddles
    if my_ball.xcor() > (window_width/2) - 20 :
        left_paddle_score.add_points()
        my_ball.reset_ball("left")
    elif my_ball.xcor() < (-(window_width/2)) + 20 :
        right_paddle_score.add_points()
        my_ball.reset_ball("right")

my_screen.exitonclick()