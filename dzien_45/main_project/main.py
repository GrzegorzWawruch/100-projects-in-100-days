from bs4 import BeautifulSoup
import requests

response = requests.get(url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
films_web_page = response.text
soup = BeautifulSoup(films_web_page, 'html.parser')
all_films = soup.find_all('div', class_='article-title-description__text')

film_dict = {}
title_with_number = []

for film in all_films:
    title_and_number = film.find( class_='title').getText()
    title_with_number.append(title_and_number)

    number_str = title_and_number.split()[0]
    title = title_and_number.replace(f'{number_str} ', '')

    if number_str == "12:":
        number_str = number_str.replace(':', '')
        number = int(number_str)
    else:
        number_str = number_str.replace(')', '')
        number = int(number_str)

    film_dict[number] = title

sorted_film_dict = dict(sorted(film_dict.items()))

with open("film_list.txt", "w", encoding="utf-8") as film_list_file:
    for film in sorted_film_dict:
        film_list_file.write(f"{film} {sorted_film_dict[film]}\n")

