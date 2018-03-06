import requests
from bs4 import BeautifulSoup


def football_info():
    url = 'https://en.wikipedia.org/wiki/National_Football_League'
    info_raw = requests.get(url)
    info_txt = info_raw.text
    info_soup = BeautifulSoup(info_txt, 'html.parser')
    return info_soup


def get_image_link():
    info_soup = football_info()
    for image in info_soup.find_all('a', {'class': 'image'}):
        image_link = 'https://en.wikipedia.org' + image.get('href')
        print(image_link)


def get_teams(info_soup):
    table = info_soup.find('table', {'class': 'navbox plainrowheaders wikitable'})
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            for division in cell.find_all('b'):
                print(division.text)


def get_division(info_soup):
    table = info_soup.find('table', {'class': 'navbox plainrowheaders wikitable'})
    for row in table.find_all('tr'):
        # print(row)
        for cell in row.find_all('a', {'title': 'AFC South'}):
            print(cell.text)
            # # for division in cell.find_all('td')[1:4]:
            # print(cell)
            # for division_name in cell.find_next_siblings('a', 'title'):
            #     print(division_name)


get_division(football_info())
