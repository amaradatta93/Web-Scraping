import requests
from bs4 import BeautifulSoup


def football_info():
    url = 'https://en.wikipedia.org/wiki/National_Football_League'
    info_raw = requests.get(url)
    info_txt = info_raw.text
    info_soup = BeautifulSoup(info_txt, 'html.parser')
    print(info_soup)


def get_image_link(info_soup):
    for image in info_soup.find_all('a', {'class': 'image'}):
        image_link = 'https://en.wikipedia.org' + image.get('href')
        print(image_link)


def get_south_teams(info_soup):
    table = info_soup.find('table', {'class': 'navbox plainrowheaders wikitable'})
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            for division in cell.find_all('b'):
                print(division.text)


football_info()
