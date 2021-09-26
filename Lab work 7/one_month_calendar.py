"""
This module returns a calendar for one month.
"""
import calendar as c
import textwrap
def weekday_name(number):
    """
    int -> str
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    if number < 1 or number > 6:
        result = None
    else:
        week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        result = week_days[number]
    return result

def weekday(date):
    """
    str -> int
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    splited_date = date.split(".")
    year_1 = int(splited_date[2])
    month_1 = int(splited_date[1])
    day = int(splited_date[0])
    return int(str(c.weekday(year_1, month_1, day))[:1])

def calendar(month_1: int, year_1: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    result = ""
    textcal = c.TextCalendar()
    result += textcal.formatmonth(year_1, month_1, w=3, l=0)[:-1]
    result = result[20:]
    if result[0] == '\n':
        result = result[1:]
    return result.lower()
print(calendar(10, 2020))
def transform_calendar(calendar1: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    new_calendar = calendar1
    new_calendar = new_calendar.split('\n')
    result = list()
    if new_calendar[0] == '':
        new_calendar = new_calendar[2:]
    else:
        new_calendar = new_calendar[1:]
    for element in new_calendar:
        devided_text = textwrap.wrap(element, 3)
        list_of_nums = list()
        for parts in devided_text:
            parts = int(parts)
            list_of_nums.append(parts)
        result.append(list_of_nums)
    full_combs = list()
    if len(result[0]) < 7:
        for _ in range(7 - len(result[0])):
            result[0].insert(0, ' ')
    for part in result:
        for symbol in part:
            symbol = str(symbol)
            full_combs.append(symbol)
    result = list()
    list_month = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    counter = 0
    for day in list_month:
        for days_in_month in range(7):
            try:
                day += " " + full_combs[counter + 7 * days_in_month]
            except IndexError:
                break
        result.append(day)
        counter += 1
    result = "\n".join(result)
    return result

if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)
