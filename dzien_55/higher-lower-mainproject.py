from flask import Flask
import random

rand_number = random.randint(0, 10)
app = Flask(__name__)

@app.route('/')
def start():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc21qYjB0Nng1NTlzMHJpb29vN3o5M2hta3p6ZGo3NXRrdGlhbDgwaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1cRMvxsxyRnaPoVkAF/giphy.gif">'

@app.route('/<int:number>')
def guess(number):
    if number == rand_number:
        return ('<h1>You found me!</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHRsZm9wdjIxYWxob2kwb2t2Z3UzajNrbzFoZ3ljc3o1OHB4ZWE1cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xDd7UQJcd3Z16FZqvu/giphy.gif">')
    elif number > rand_number:
        return ('<h1> Too high, try again!</h1>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXBjYmF2ejkxajMzZ3NwODY2eXFmenM5MGRrbDRqdXM0YWI4YmZ5eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vTZX0SD5A0BoY/giphy.gif>')
    elif number < rand_number:
        return ('<h1> Too low, try again!</h1>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHh6NTIzbTAzOWswZWZsaXFjcjFxOTRxcGNoMm1sM2toYmg2M2x2bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif">')

if __name__ == '__main__':
    app.run(debug=True)