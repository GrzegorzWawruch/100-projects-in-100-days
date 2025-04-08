from flask import Flask
from flask import render_template
import random
import datetime
import requests
app = Flask(__name__)

@app.route('/')
def home():
    data = datetime.datetime.now().strftime('%Y')
    random_number = random.randint(1, 10)
    return render_template("index.html", random_number=random_number, year=data)

@app.route('/guess/<name>')
def guess(name):
    genderize_response = requests.get(url='https://api.genderize.io', params={'name':name})
    gender = genderize_response.json().get('gender')
    age_response = requests.get(url='https://api.agify.io', params={'name':name})
    age = age_response.json().get('age')
    return render_template("info.html", name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)