import os

from flask import Flask
from flask import render_template
from flask import request
from dotenv import load_dotenv
import posts
import smtplib

app = Flask(__name__)

POSTS_API_URL = "https://api.npoint.io/f570b284b357afcceb0f"
posts_list = posts.create_posts_objects_from_api(POSTS_API_URL)

load_dotenv()

MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']
RECIPIENT_EMAIL = os.environ['RECIPIENT_EMAIL']

@app.route('/')
def home():
    return render_template('index.html', posts=posts_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        print(f"{name}\n{email}\n{phone}\n{message}")

        #send mail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"Subject: Message from page\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}"
            )

        return render_template('contact.html', message=True)

    elif request.method == 'GET':
        return render_template('contact.html', message=False )

@app.route('/post/<int:id>')
def post(id):
    for elm in posts_list:
        if elm.id == id:
            requested_post = elm
    return render_template('post.html', post=requested_post)



if __name__ == '__main__':
    app.run(debug=True)