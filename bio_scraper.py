import requests
from bs4 import BeautifulSoup


url = "https://www.biography.com/crime-figure"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
profiles = soup.find_all("a", {"class": "m-card--image-link"})

for profile in profiles:
    print(profile["title"] + "\n")
    url = "https://www.biography.com/" + profile["href"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    desc = soup.find("div", {"class":"m-person--abstract l-person--abstract"})
    print(desc.text + "\n")

    synopsis = soup.find("section", {"class": "m-detail--body l-person--body"})
    parts = synopsis.findChildren(["h2","p"])
    for part in parts:
        print(part.text + "\n")
