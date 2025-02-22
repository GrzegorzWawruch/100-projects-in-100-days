import random
import stages_library



glossary = ['brick','snowman', 'castle']
word = random.choice(glossary)
chances = 7
word_status = []
player_word = ""

for i in range(len(word)):
    word_status += '_'

def print_word_status():
    print('You word is: ', end="")
    for j in range(len(word)):
        print(word_status[j], end="")
    print("\n")


print('Welcome to HANDMAN Game \n')

while chances > 0:
    print_word_status()
    player_vote = input('type the letter: ')

    if player_vote in word:
        print("Good choice, your letter is in word. Look at your hangman status !")

        for k in range(len(word)):
            if word[k] == player_vote:
                word_status[k] = player_vote

                print(stages_library.stages[7 - (chances % 7)])

        if "_" not in word_status:
            print("Congratulations, you won!")
            chances = 0



    else:
        print("Bad choice, your letter isn\'t in word. Look at your hangman status !")
        chances -= 1
        print(stages_library.stages[7 - (chances % 7)])
        if chances == 0:
            print("Game over")

