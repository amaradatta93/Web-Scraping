from utils import get_parser, str_to_int, convert_to_dictionary, parse_coordinates


def get_table(url):
    info_soup = get_parser(url)
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


def get_coordinates(geo_table):
    coordinates_list = []
    for row in geo_table.find_all('span', {'class': 'geo-dec'}):
        coordinates_list.append(parse_coordinates(row.string))

    return coordinates_list


def find_stadiums_within_seat_range(min_seats, max_seats, url):
    table = get_table(url)
    list_map = convert_to_dictionary(get_football_teams(table), get_stadium_capacity(table))
    for team in list_map:
        if (list_map[team] >= min_seats) and (list_map[team] <= max_seats):
            print("{0}: {1}".format(team, str(list_map[team])))


def find_teams_with_bounds(latitude, longitude, url):
    coord_table = get_table(url)
    coordinates_map_to_team = convert_to_dictionary(get_football_teams(coord_table), get_coordinates(coord_table))
    for i in coordinates_map_to_team:
        if (coordinates_map_to_team[i][0] >= latitude) or (coordinates_map_to_team[i][1] >= longitude):
            print(i + ': ' + str(coordinates_map_to_team[i][0]) + '°N, ' + str(coordinates_map_to_team[i][1]) + '°W')
