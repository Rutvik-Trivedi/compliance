from bs4 import BeautifulSoup
import requests

class Scrapper():

    def __init__(self) -> None:
        pass
        
    def parse(self, url):
        page = requests.get(url).content
        soup = BeautifulSoup(page, 'html.parser')
        paragraphs = soup.find_all('p')
        paragraphs = [p.get_text() for p in paragraphs]
        return paragraphs