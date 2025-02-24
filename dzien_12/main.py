import random

guesses = 0
number_to_guess = random.randint(1, 100)

while True:

    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    if level == 'easy':
        guesses = 10
    elif level == 'hard':
        guesses = 5

    while guesses > 0:
        print(f'You have {guesses} attempts to guess the number.')
        input_guess = int(input('Make a guess: '))
        if input_guess == number_to_guess:
            print('Correct, you won the game !')
            play_again = input('Would you like to play again? ')
            if play_again == 'yes':
                break
            elif play_again == 'no':
                exit()
        elif input_guess > number_to_guess:
            guesses -= 1
            print('Too high, try again.')
        elif input_guess < number_to_guess:
            guesses -= 1
            print('Too low, try again.')

    print('You doesn\'t have a chance')
    play_again = input('Would you like to play again? (yes/no): ')
    if play_again == 'yes':
        continue
    elif play_again == 'no':
        exit()
