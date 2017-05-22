#!/usr/bin/env python3

import requests
from datetime import datetime
import sys
import bs4


def main():
    url = get_url()
    # Downloads request from url URL and stores as string in res
    res = requests.get(url)
    # Creates Beautiful Soup out of html
    current_soup = bs4.BeautifulSoup(res.text, "lxml")
    # Takes all <tr> tags
    elems = current_soup.select('tr')

    console_out(elems[14].getText().strip())


def console_out(booking):
    if booking:
        print('\nIt is not free, there is\n \n' + booking + '\n')
    else:
        print("\nThis is currently free\n")


def get_url():
    baseurl = 'https://www101.dcu.ie/timetables/feed.php?'
    if len(sys.argv) == 1:
        room = input("Please enter a vailid room number eg. GLA.LG26\n")
    else:
        room = sys.argv[1]
    week = get_week()
    hour = get_hour()
    day = get_day()
    template = 'location'
    return ('%sroom=%s&week1=%s&hour=%s&day=%s&template=%s'
            % (baseurl, room, week, hour, day, template))


def get_week():
    # Stub must replace
    week_number = 20
    return week_number


def get_day():
    date = datetime.today()
    return date.strftime("%w")


def get_hour():
    date = datetime.now()
    return str(date).split()[1][0:2]


if __name__ == '__main__':
    main()
