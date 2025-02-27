import random


def get_object_to_compare(list_of_choices, dictionary):

    while True:
        choice = random.randint(0,len(dictionary)-1)

        if choice not in list_of_choices:
            list_of_choices.append(choice)
            return choice


