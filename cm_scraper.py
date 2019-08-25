import requests
from bs4 import BeautifulSoup


url = "https://criminalminds.fandom.com/wiki/Real_Criminals/Serial_Killers"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
profiles = soup.find_all("div", {"class": "lightbox-caption"})

for profile in profiles:
    print(profile.find("a")["title"] + "\n")
    url = "https://criminalminds.fandom.com" + profile.find("a")["href"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    desc = soup.find("div", {"id":"mw-content-text"})
    print("Quote:\n" + desc.find("table").text.strip() + "\n")

    ps = desc.find_all("p")
    for p in ps:
        print(p.text)
    break
