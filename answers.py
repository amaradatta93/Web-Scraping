from stadium import find_stadiums_within_seat_range, find_teams_with_bounds


def print_divider():
    print('-----------------------------------------------------------------------------')


LINK = 'https://en.wikipedia.org/wiki/National_Football_League'

# Question 1 params
STADIUM_MIN_SEATING = 50000
STADIUM_MAX_SEATING = 80000

# Question 2 Params
LATITUDE = 39
LONGITUDE = 84

find_stadiums_within_seat_range(STADIUM_MIN_SEATING, STADIUM_MAX_SEATING, LINK)
print_divider()
find_teams_with_bounds(LATITUDE, LONGITUDE, LINK)