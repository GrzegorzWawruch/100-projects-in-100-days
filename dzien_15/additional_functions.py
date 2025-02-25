import db


def insert_coins(product):
    quarters = float(input('How many quarters?: '))
    dimes = float(input('How many dimes?: '))
    nickles = float(input('How many nickles?: '))
    pennies = float(input('How many pennies?: '))

    sum_of_money = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles)+ (0.01 * pennies)

    rest = round((sum_of_money - db.MENU[product]['cost']),2)


    moneys = float(0)
    moneys += round((sum_of_money - rest),2)

    print(f'Here is ${rest} in change. ')
    return moneys

def sources_subtraction(product):
    if db.MENU[product]['ingredients']['water'] < db.resources['water']:
        if db.MENU[product]['ingredients']['milk'] < db.resources['milk']:
            if db.MENU[product]['ingredients']['coffee'] < db.resources['coffee']:
                db.resources['water'] -= db.MENU[product]['ingredients']['water']
                db.resources['milk'] -= db.MENU[product]['ingredients']['milk']
                db.resources['coffee'] -= db.MENU[product]['ingredients']['coffee']
                return True
            else:
                print(f'Sorry there is not enough coffee.')
                return False
        else:
            print(f'Sorry there is not enough milk.')
            return False
    else:
        print(f'Sorry there is not enough water.')
        return False





