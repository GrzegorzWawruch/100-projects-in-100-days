import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you have in your password ?\n"))
nr_numbers = int(input("How many numbers would you have in your password ?\n"))
nr_symbols = int(input("How many symbols would you have in your password ?\n"))

password_chars =[]
for letter in range (nr_letters):
    random_index = random.randint(0, len(letters)-1)
    password_chars += letters[random_index]

for number in range (nr_numbers):
    random_index = random.randint(0, len(numbers)-1)
    password_chars += numbers[random_index]

for symbol in range (nr_symbols):
    random_index = random.randint(0, len(symbols)-1)
    password_chars += symbols[random_index]

print(password_chars)
random.shuffle(password_chars)
print(password_chars)

password = ""

for i in password_chars:
    password += i

print(f'Your password is {password}')


