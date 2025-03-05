import pandas
from game_screen import *

create_screen(my_screen)
game_is_on = True

data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()
game_status = 0
print(states_list)

while game_is_on and game_status < 50:
    on_screen_click()
    answer = my_screen.textinput(title= f"{game_status}/50States Correct", prompt="What's another state's name?")
    answer = answer.title()
    if answer == "Exit":
        exit()
    elif answer in states_list:
        game_status += 1
        state = data[data["state"] == answer]
        x = int(state.x)
        y = int(state.y)
        write_state_name_on_map(answer, x, y)

exit_on_click(my_screen)