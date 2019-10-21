import requests
from bs4 import BeautifulSoup
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))
from elastic import es_insert


# Retrieve all pages
url = "https://www.bizarrepedia.com/crime/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
pages = int(soup.find("a", {"data-num-pages": True})["data-num-pages"])

for page in range(1, pages + 1):
    if page == 1: # First page has no page number
        url = "https://www.bizarrepedia.com/crime"
    else:
        url = "https://www.bizarrepedia.com/crime/page/" + str(page)
 
    # Retrieve each story
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    stories = soup.find_all("a", {"class": "bx"})

    for story in stories:
        response = requests.get(story["href"])
        soup = BeautifulSoup(response.text, "lxml")
        subject = soup.find("h1", {"class": "entry"}).text
        main_story = soup.find("div", {"class": "typography"})
        blocks = main_story.find_all("p")
        full_story = ""

        for block in blocks:
            full_story = full_story + block.text + "\n\n"
        print(subject + "\n\n" + full_story)
        es_insert("truecrime", "bizarrepedia", subject, full_story)
