import requests
from bs4 import BeautifulSoup
from elastic import *


# Retrieve all stories
url = "https://criminalminds.fandom.com/wiki/Real_Criminals/Serial_Killers"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
stories = soup.find_all("div", {"class": "lightbox-caption"})

for story in stories:
    # Retrieve each story
    url = "https://criminalminds.fandom.com" + story.find("a")["href"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    main_story = soup.find("div", {"id":"mw-content-text"})
    subject = story.find("a")["title"]
    if main_story.find("table") is not None:
        quote = " ".join(main_story.find("table").text.split())
    blocks = main_story.find_all("p")
    full_story = ""

    for block in blocks:
        full_story = full_story + block.text + "\n"

    print(quote + "\n" + subject + "\n\n" + full_story)
    es_insert("truecrime", "criminalminds", subject, full_story, quote=quote)
