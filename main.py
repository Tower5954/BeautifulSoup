from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()
    
    
soup = BeautifulSoup(contents, 'html.parser')
# -- what the full title looks like -- #
# print(soup.title)
# -- what the name of it is -- #
# print(soup.title.name)
# -- the string that is in the brackets -- #
# print(soup.title.string)
# -- print the whole thing -- #
# print(soup)
# -- indent it to make it easier to read
# print(soup.prettify())

# -- Finding all of some tag i.e all of the paragraph -- #

all_p_tags = soup.find_all(name='p')
# print(all_p_tags)
#
all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

# all_href_tags = soup.find_all(name='href') #~~ this doesnt work!!! ~~#
# print(all_href_tags)

# -- If you want something in a tag, create a for loop -- #
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get('href'))

# -- to pin-point a specific class in a tag -- #
# heading = soup.find(name='h1', id="name")
# print(heading)

# -- if you try to look for a "class" you MUST write it as class_ because class is a reserved word -- #
new_heading = soup.find(name='h3', class_='heading')
print(new_heading)