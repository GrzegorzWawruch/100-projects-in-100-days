
if_continue = True
prices = {}
highest_price = 0
winner = ""

print('Welcome to the secret auction program !')

while if_continue:

    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))

    prices[name] = bid

    want_continue = input('Are there any other bidders? (y/n): ')
    if want_continue == 'y':
        continue
    elif want_continue == 'n':

        for key in prices:
            if prices[key] > highest_price:
                winner = key

    print(f'The winner is {winner}, he/she offer {prices[winner]}$')

    break

