from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
title_text = []
for titles in titles:
    text = titles.getText()
    title_text.append(text)

films = title_text[::-1]


with open("movies.txt", mode="w", encoding="utf-8")as file:
    for movies in films:
        file.write(f"{movies}\n")

# - - - List Comprehension - - - #
# movie_titles = [movie.getText() for movie in titles]

# - - - OR - - - #
#
# for n in range(len(titles) - 1, -1, -1):
#     print(titles[n])
