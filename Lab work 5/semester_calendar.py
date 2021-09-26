import calendar
def semester_calendar(output_type, year, first_month, last_month):
    r"""
    (str, int, int, int) -> str
    Function builds semester calender in txt and html (HTML table) view.
    >>> semester_calendar("txt", 2016, 2, 3) # doctest: +ELLIPSIS
    '   February...31\n'
    >>> semester_calendar("html", 2016, 2, 3) # doctest: +ELLIPSIS
    '<table border="0"...class="noday">&nbsp;</td></tr>\n</table>\n'
    """
    if type(year) == str or type(first_month) == str or type(last_month) == str:
        return None
    number_of_calendars = last_month - first_month
    num_of_tries = 0
    if output_type == "html":
        s = ""
        htmlcal = calendar.HTMLCalendar()
        while True:
            if number_of_calendars >= num_of_tries:
                s += htmlcal.formatmonth(year, first_month)
            else:
                break
            num_of_tries += 1
            first_month += 1
    if output_type == "txt":
        s = ""
        htmlcal = calendar.TextCalendar()
        while True:
            if number_of_calendars >= num_of_tries:
                s += htmlcal.formatmonth(year, first_month)
            else:
                break
            num_of_tries += 1
            first_month += 1
    return s
