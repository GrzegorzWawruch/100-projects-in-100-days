from flask import Flask
from flask import render_template
import posts
app = Flask(__name__)

POSTS_API_URL = "https://api.npoint.io/f570b284b357afcceb0f"
posts_list = posts.create_posts_objects_from_api(POSTS_API_URL)

@app.route('/')
def home():
    return render_template('index.html', posts=posts_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    for elm in posts_list:
        if elm.id == id:
            requested_post = elm
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)