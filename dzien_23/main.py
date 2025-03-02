from my_screen import *
from player import Player
from car import CarManager
from score import Score

my_player = Player()
my_score = Score()
game_is_on = True
window_height = screen_height(my_screen)
window_width = screen_width(my_screen)
cars= CarManager()
create_screen(my_screen)
my_player.set_start_player_position(window_height)

while game_is_on:
    my_score.write_score(window_height, window_width)
    cars.create_cars(window_height, window_width)
    cars.move_cars()
    key_detection(my_screen, my_player.move_up, my_player.move_left, my_player.move_right)
    screen_update(my_screen)

    #Detect collision with cars
    for car in cars.cars:
        player_left, player_right, player_top, player_bottom = my_player.get_edges()
        car_left, car_right, car_top, car_bottom = cars.get_edges(car)

        if my_player.heading() == 90:
            if (abs(car_right) > abs(player_right) > abs(car_left) and abs(car_bottom) < abs(player_top) < abs(car_top)) or ( abs(car_left) > abs(player_left) > abs(car_right) and abs(car_bottom) < abs(player_top) < abs(car_top)):
                print('collision')
                my_score.write_end_game()
                game_is_on = False
                break
        elif my_player.heading() == 0:
            if (abs(car_top) > abs(player_left) > abs(car_bottom) and abs(car_right) < abs(player_top) < abs(car_left)) or (abs(car_bottom) < abs(player_right) < abs(car_top) and abs(car_left) < abs(player_top) < abs(car_right)):
                print('collision')
                my_score.write_end_game()
                game_is_on = False
                break
        elif my_player.heading() == 180:
            if ( abs(car_top) > abs(player_right) > abs(car_bottom) and abs(car_right) > abs(player_top) > abs(car_left)) or ( abs(car_bottom) < abs(player_left) < abs(car_top) and abs(car_left) > abs(player_top) > abs(car_right)):
                print('collision')
                my_score.write_end_game()
                game_is_on = False
                break

    #Detect point/ player end level
    if my_player.ycor() > round((window_height/2) * 0.92):
        my_score.add_score()
        my_player.set_start_player_position(window_height)
        cars.new_level_parameters()

exit_from_the_screen(my_screen)