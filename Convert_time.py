import re
def main():
    date = input('Date in M/D/Y or Month Day, Year:').strip().lower()
    print(convert_date(date))
def convert_date(date):
    month_list= {
        'january':1,
        'february':2,
        'march':3,
        'april':4,
        'may':5,
        'june':6,
        'july':7,
        'august':8,
        'september':9,
        'october':10,
        'november':11,
        'december':12
    }

    date_match = re.search(r'^([A-Za-z]+) ([0-9]{1,2}), ([0-9]{4})$', date)
    if date_match:
        months = date_match.group(1)
        day = int(date_match.group(2))
        year = int(date_match.group(3))
        if months in month_list:
            month = month_list[months]
            return f'{year}-{month:02}-{day:02}'

    matches = re.search(r'^([1-9]|1[0-2])/([0-2][0-9]|3[0-1])/([0-9]{4})$', date)

    if matches:
        months, days, years = matches.group(1), matches.group(2), matches.group(3)
        return f'{years}-{int(months):02}-{int(days):02}'
    else:
        return 'invalid'




if __name__ == '__main__':
    main()