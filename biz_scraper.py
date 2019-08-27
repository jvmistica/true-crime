import requests
from bs4 import BeautifulSoup


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
 
    # Retrieve each article
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    articles = soup.find_all("article", {"class": "not_mod"})

    for article in articles:
        # Retrieve each story
        response = requests.get(article.a["href"])
        soup = BeautifulSoup(response.text, "lxml")
        subject = soup.find("h1", {"class": "entry"}).text
        story = soup.find("div", {"class": "typography"})
        blocks = story.find_all("p")

        for block in blocks:
            print(block.text + "\n")
        break
    break
