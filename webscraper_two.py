from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(name='a', class_='storylink')
article_link = article_tag.get('href')
article_upvote = soup.find(name='span', class_='score')

print(article_tag.getText())
print(article_link)
print(article_upvote.getText())