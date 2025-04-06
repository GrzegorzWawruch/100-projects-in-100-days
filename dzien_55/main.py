from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def make_bold_function():
        return "<b>" + function() + "</b>"
    return make_bold_function

def make_italic(function):
    def make_italic_function():
        return "<i>" + function() + "</i>"
    return make_italic_function

def make_underline(function):
    def make_underline_function():
        return "<u>" + function() + "</u>"
    return make_underline_function


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmY2YWExd2xhZnMwOWR3bTYxbmxuNHY5cGI5d3JxMTYxbDJwampjeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/quQijRpxpy7UQ/giphy.gif">'
            '')

@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'Bye!'

# @app.route("/<name>")
# def greet(name):
#     return f"Hello {name}"


# @app.route("/username/<path:name>")
# def greet(name):
#     return f"Hello {name}"




if __name__ == '__main__':
    app.run(debug=True) #run app in debug mode allow us to auto-reaload the app

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User('John')
new_user.is_logged_in = True
create_blog_post(new_user)

@app.route("/username/<name>/<int:number>")
def username(name,number):
    return f"Hello {name}, you are {number} tears old!"

username()