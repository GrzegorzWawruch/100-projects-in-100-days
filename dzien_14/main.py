import art
import game_data
import os
from additional_functions import *

os.system('cls')
Compare_A = ""
Compare_B = ""
was = []
player_score = 0


while True:
    os.system('cls')
    Compare_A = get_object_to_compare(was, game_data.data)

    while True:

        if player_score > 0:
            print(f'You are right! Current score: {player_score}.')
        Compare_B = get_object_to_compare(was, game_data.data)
        print(art.logo)
        print(f'Compare A: {game_data.data[Compare_A]['name']}, a {game_data.data[Compare_A]['description']}, from {game_data.data[Compare_B]['country']}')
        print(art.vs)
        print(f'Compare B: {game_data.data[Compare_B]['name']}, a {game_data.data[Compare_B]['description']}, from {game_data.data[Compare_B]['country']}')
        player_choice = input(f'Who has more followers? \'A\' or \'B\': ')

        if (game_data.data[Compare_A]['follower_count'] > game_data.data[Compare_B]['follower_count']) and player_choice == 'A':
            player_score += 1
            os.system('cls')
        elif (game_data.data[Compare_A]['follower_count'] < game_data.data[Compare_B]['follower_count']) and player_choice == 'A':
            os.system('cls')
            print(f'Sorry, that\'s wrong. Final score: {player_score}')
            player_score = 0
            break
        elif (game_data.data[Compare_B]['follower_count'] > game_data.data[Compare_A]['follower_count']) and player_choice == 'B':
            player_score += 1
            Compare_A = Compare_B
            os.system('cls')
        elif (game_data.data[Compare_B]['follower_count'] < game_data.data[Compare_A]['follower_count']) and player_choice == 'B':
            os.system('cls')
            print(f'Sorry, that\'s wrong. Final score: {player_score}')
            player_score = 0
            break
