from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    decision = input(f'What would you like (espresso/latte/cappuccino): ')
    if decision == 'report':
        coffee_maker.report()
        money_machine.report()
    elif decision == 'off':
        break
    else:
        drink = menu.find_drink(decision)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
