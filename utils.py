import requests
from bs4 import BeautifulSoup


def get_parser(url):
    info_raw = requests.get(url)
    info_txt = info_raw.text
    info_soup = BeautifulSoup(info_txt, 'html.parser')
    return info_soup


def str_to_int(number_str):
    str(number_str)
    numeric = number_str.replace(',', '')
    return int(numeric)


def convert_to_dictionary(list_1, list_2):
    key_value_pair = dict(zip(list_1, list_2))
    return key_value_pair


def parse_coordinates(coordinate_string):
    """
    Given a string in the format "<LATITUDE>°<D> <LONGITUDE>°<D>", returns the decimal values for <LATITUDE> and <LONGITUDE>
    """
    coordinates = coordinate_string.split(' ')
    return float(coordinates[0].replace('°N', '')), float(coordinates[1].replace('°W', ''))
