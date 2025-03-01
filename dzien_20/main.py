from Blocks import *
from Screen import *
from Food import *
from Score import *

food = Food()
my_screen = create_screen()
my_snake = Snake()
score = Score()
food.move_food()
score.paint_upper_border()
game_is_on = True

while game_is_on:

    my_snake.head.forward(20)
    screen_update(my_screen)
    key_detection(my_snake.turn_left, my_snake.turn_right, my_snake.turn_up, my_snake.turn_down, my_screen)

    #Detect collision with food
    if my_snake.head.distance(food) < 20:
        my_snake.add_block_to_blocks_list()
        food.move_food()
        score.add_points()

    #Detect collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 240 or my_snake.head.ycor() < -280:
        score.end_game()
        game_is_on = False
        break

    #Detect collision with tail
    for block in my_snake.blocks:
        if block == my_snake.head:
            pass
        elif my_snake.head.distance(block) < 10:
            score.end_game()
            game_is_on = False
            break

    my_snake.move_blocks()

exit_from_the_screen(my_screen)