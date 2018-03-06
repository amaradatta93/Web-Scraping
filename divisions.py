from utils import get_table


def parse_table(table, division_search):
    division = {}
    current_division = ''
    for row in table.find_all('tr'):
        children_count = 0
        th_count = 0
        heading = ""
        for c in row.find_all(["th", "td"]):
            children_count += 1
            if c.name == 'th':
                th_count += 1
                heading = c.text

        # This is row is the conference row => skip
        if children_count == 1 and th_count == 1:
            continue
        # This is row is the division row => update the current division
        elif children_count > 1 and th_count == 1:
            current_division = heading
        # This is row is the first row - title row => skip
        elif children_count > 1 and th_count > 1:
            continue

        # If the row is not skipped => team row
        curr_row = []
        for c in row.find_all("td"):
            if c.string:
                curr_row.append(c.string)
            else:
                a = row.find("a")
                if a:
                    curr_row.append(a.text)

        if current_division not in division:
            division[current_division] = []

        division[current_division].append(curr_row)

    for team in division[division_search]:
        print(team[0])


def find_teams_in_division(division, url):
    parse_table(get_table(url), division)
