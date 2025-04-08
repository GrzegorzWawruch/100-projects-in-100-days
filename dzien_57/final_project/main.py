from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

blogs_response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
blogs_posts = blogs_response.json()
posts = []
for post in blogs_posts:
    posts.append(Post(post['id'], post['title'], post['subtitle'], post['body']))

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def show_post(id):
    request_post = None
    for post in posts:
        if post.id == id:
            request_post = post
    return render_template('post.html', post=request_post)

if __name__ == "__main__":
    app.run(debug=True)
