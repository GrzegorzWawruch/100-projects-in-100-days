import requests

class Post():
    def __init__(self,id ,title ,subtitle, content):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.content = content

def create_posts_objects_from_api(url):
    response = requests.get(url)
    response = response.json()

    posts_list = []

    for items in response:
        post = Post(items['id'],items['title'],items['subtitle'],items['body'])
        posts_list.append(post)

    return posts_list