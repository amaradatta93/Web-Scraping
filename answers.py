from divisions import find_teams_in_division
from images import get_image_link
from stadium import find_stadiums_within_seat_range, find_teams_with_bounds


def print_divider():
    print('-----------------------------------------------------------------------------')


LINK = 'https://en.wikipedia.org/wiki/National_Football_League'

# Question 1 params
LATITUDE = 39
LONGITUDE = 84

# Question 2 params
DIVISION = 'South'

# Question 3 Params
STADIUM_MIN_SEATING = 50000
STADIUM_MAX_SEATING = 80000


# Question 1
find_teams_with_bounds(LATITUDE, LONGITUDE, LINK)
print_divider()

# Question 2
find_teams_in_division(DIVISION, LINK)
print_divider()

# Question 3
find_stadiums_within_seat_range(STADIUM_MIN_SEATING, STADIUM_MAX_SEATING, LINK)
print_divider()

# Question 4
get_image_link(LINK)
