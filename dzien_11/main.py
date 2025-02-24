from functions import *

players_db = {"player": [],
              "computer": []}
Play = True

print('Welcome in blackjack !')
while True:

        get_first_cards(players_db)
        print_cards(players_db, "player")
        print_cards(players_db, "computer")


        while Play:
            player_want_more_cards = input('Type \'y\' to get another card, type \'n\' to pass: ')
            if player_want_more_cards == 'y':
                add_card_to_player(players_db)
                print_cards(players_db, "player")
                if(check_cards(players_db, "player")) == "good":
                    continue
                elif(check_cards(players_db, "player")) == "too_high":
                    print(f'You lose, because sum of your cards is {sum(players_db["player"])}')
                    want_play_again =  input('Would you like to play again? (y/n): ')
                    if want_play_again == 'y':
                        reset_cards(players_db)
                        break
                    elif want_play_again == 'n':
                        exit()

            elif player_want_more_cards == 'n':
                print(f'Your cards sum is {sum(players_db["player"])}, now computer playing')
                computer_gets_more_cards(players_db)
                print_cards(players_db, "player")
                print_cards(players_db, "computer")
                if (sum(players_db["player"]) > sum(players_db["computer"])) and sum(players_db["player"]) <= 21:
                    print(f'You wins!')
                    want_play_again =  input('Would you like to play again? (y/n): ')
                    if want_play_again == 'y':
                        reset_cards(players_db)
                        break
                    elif want_play_again == 'n':
                        exit()
                elif (sum(players_db["player"]) < sum(players_db["computer"])) and sum(players_db["computer"]) <= 21:
                    print(f'Computer wins!')
                    want_play_again =  input('Would you like to play again? (y/n): ')
                    if want_play_again == 'y':
                        reset_cards(players_db)
                        break
                    elif want_play_again == 'n':
                        exit()
