from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.tutorialbar.com/the-python-programming-comprehensive-bootcamp/'
# url = 'https://www.pastelink.net/ij7aau87'
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
title = soup.title
# print(type(title))
# print(type(title.string))

# htmls = soup.find('p').get_text()
# print(htmls)
anchors = soup.find_all('a')
# for link in anchors :
#     ud = link.get('href')
#     print(ud)

    # print('yes')
for link in soup.find_all('a',
                          attrs={'href': re.compile("udemy.com")}):
    ud = link.get('href')
    print(ud)