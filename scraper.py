import requests
from bs4 import BeautifulSoup


def get_numpages(soup):
    numpages = soup.find("a", {"data-num-pages": True})
    return int(numpages["data-num-pages"])

def get_links(soup):
    articles_list = list()
    articles = soup.find_all("article", {"class": "not_mod"})
    for article in articles:
        articles_list.append(article.a["href"])
    return articles_list

def get_stories(link):
    full_story = ""
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")
    subject = soup.find("h1", {"class": "entry"}).text
    story = soup.find("div", {"class": "typography"})
    blocks = story.find_all("p")
    
    for block in blocks:
        full_story = full_story + block.text + "\n"
    return dict({subject: full_story})


url = "https://www.bizarrepedia.com/crime/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
pages = get_numpages(soup)
links = list()

for page in range(1, pages + 1):
    # First page has no page number for Bizarrepedia
    if page == 1:
        url = "https://www.bizarrepedia.com/crime"
    else:
        url = "https://www.bizarrepedia.com/crime/page/" + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    links.extend(get_links(soup))

for link in links:
    print(get_stories(link))
