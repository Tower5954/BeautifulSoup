from bs4 import BeautifulSoup
import requests

# - - -  The basics - - - #
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup.h1.string)

response = requests.get("https://news.ycombinator.com/shownew")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# print(soup.title)

# - - - Finding the first occurrence on the site - - - #

# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.get_text()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").get_text()
#
# print(article_tag)
# print(article_text)
# print(article_link)
# print(article_upvote)

# - - - Finding all occurrences - - - #
articles = soup.find_all(name="a", class_="storylink")
articles_text = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_text.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(articles_text[19])
print(articles_links[19])
print(article_upvotes[19])
# - - - OR - - - #
# print(articles_text[largest_index])
# print(articles_links[largest_index])
# print(article_upvotes[largest_index])

# - - - to get just the numbers in the 'points' from upvotes - - - #
# print(int(article_upvotes[].split()[]))