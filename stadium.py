import requests
from bs4 import BeautifulSoup


def get_table(url):
    info_raw = requests.get(url)
    info_txt = info_raw.text
    info_soup = BeautifulSoup(info_txt, 'html.parser')
    table = info_soup.find('table', {'class': 'navbox plainrowheaders wikitable'})
    return table


def get_stadium_capacity(stadium_table):
    stadium_capacity = []
    for row in stadium_table.find_all('tr'):
        for cell in row.find_all('td', {'align': 'center'}):
            numeric_value = str_to_int(cell.text)
            stadium_capacity.append(numeric_value)
    return stadium_capacity


def get_football_teams(team_table):
    football_team = []
    for row in team_table.find_all('tr'):
        for cell in row.find_all('td'):
            for division in cell.find_all('b'):
                football_team.append(division.text)
    return football_team


def str_to_int(number_str):
    str(number_str)
    numeric = number_str.replace(',', '')
    return int(numeric)


def convert_to_dictionary(list_1, list_2):
    key_value_pair = dict(zip(list_1, list_2))
    return key_value_pair


def find_between_range(range_1, range_2, url_link):
    table = get_table(url_link)
    list_map = convert_to_dictionary(get_football_teams(table), get_stadium_capacity(table))
    for team in list_map:
        if (list_map[team] >= range_1) and (list_map[team] <= range_2):
            print(team + ': ' + str(list_map[team]))


def get_coordinates(geo_table):
    coordinates_list = []
    for row in geo_table.find_all('span', {'class': 'geo-dec'}):
        str(row.string)
        coordinates = str(row.string).split(' ')
        coordinates[0] = float(coordinates[0].replace('°N', ''))
        coordinates[1] = float(coordinates[1].replace('°W', ''))
        coordinates_list.append(coordinates)
    return coordinates_list


def team_coordinates_mapping(url):
    coord_table = get_table(url)
    coordinates_map_to_team = convert_to_dictionary(get_football_teams(coord_table), get_coordinates(coord_table))
    for i in coordinates_map_to_team:
        print(i + ': ' + str(coordinates_map_to_team[i]))



link = 'https://en.wikipedia.org/wiki/National_Football_League'
a = 50000
b = 80000

find_between_range(a, b, link)
# get_coordinates(get_table(link))
team_coordinates_mapping(link)
