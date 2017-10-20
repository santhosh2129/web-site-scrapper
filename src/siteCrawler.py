from bs4 import BeautifulSoup
from html.parser import HTMLParser
import pinger


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)



def parseContent(raw_content):
    rss = {}
    soup = BeautifulSoup(raw_content)
    for link in soup.find_all('link'):
        if link.get('type') == "application/rss+xml":
            rss["rss"] = link.get('href')
            return rss

def getMainContent(raw_content):
    soup = BeautifulSoup(raw_content)
    content = ""
    for link in soup.find_all('p'):
        content = content +strip_tags(link)
    return {'main_content' :  content}

def strip_tags(html):
    s = MLStripper()
    s.feed(str(html))
    return s.get_data()


def crawlURL(url):
    retrivedData = {}
    retrivedData.update(pinger.getContent(url))
    print(retrivedData)
    retrivedData.update(parseContent(retrivedData['raw_content']))
    retrivedData.update(getMainContent(retrivedData['raw_content']))
    del retrivedData['raw_content']
    return retrivedData