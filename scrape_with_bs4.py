import requests
from bs4 import BeautifulSoup

url = "https://github.com/artonmirakaj?tab=repositories"
r = requests.get(url)

#see all html content on specific requests
soup = BeautifulSoup(r.content)

links = soup.find_all("a")#find links <a>

for link in links:
    print "<a href='%s'>'%s'</a>" %(link.get("href"), link.text)
    #prints all different links and text from different link

#div class of my repositories
general_data = soup.find_all("div", {"class": "col-9 float-left pl-2"})


for item in general_data:
    try:
        print item.contents[1].find_all("div", {"id": "user-repositories-list"})
    except:
        pass

    try:
        print item.contents[1].find_all("ul", {"data-filterable-for": "your-repos-filter"})
    except:
        pass

    try:
        print item.contents[1].find_all("li", {"class": "col-12 d-block width-full py-4 border-bottom public source"})
    except:
        pass