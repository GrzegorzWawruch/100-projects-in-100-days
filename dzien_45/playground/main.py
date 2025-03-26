from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

all_spans = soup.find_all('span', class_='titleline')
all_upvotes = soup.find_all(name='span', class_='score')
article_text = []
article_link = []
article_upvote = []
for span, upvote in zip(all_spans, all_upvotes):
    title = span.find('a')
    article_text.append(title.getText())
    article_link.append(title.get('href'))
    article_upvote.append(int(upvote.getText().split()[0]))
    # print(article_text, article_link, article_upvote)


# print(article_text)
# print(article_link)
# print(article_upvote)


highest_upvote = max(article_upvote)
print(article_text[article_upvote.index(highest_upvote)])
print(article_link[article_upvote.index(highest_upvote)])


# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get('href'))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)