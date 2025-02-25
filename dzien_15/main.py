from additional_functions import *

money = float(0)
decision = ""
it_is_possible = True

while True:
    decision = input(f'What would you like (espresso/latte/cappuccino): ')
    if decision == 'report':
        print(f'Water: {db.resources['water']}\nMilk: {db.resources['milk']}\nCoffee: {db.resources['coffee']}\nMoney: {money}$')
    if decision == 'espresso':
        it_is_possible = sources_subtraction(decision)
        if it_is_possible:
            money += insert_coins(decision)
    elif decision == 'latte':
        it_is_possible = sources_subtraction(decision)
        if it_is_possible:
            money += insert_coins(decision)
    elif decision == 'cappuccino':
        it_is_possible = sources_subtraction(decision)
        if it_is_possible:
            money += insert_coins(decision)