"""
This module makes operations with brauser history.
"""


import doctest


def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date

    >>> print(sites_on_date([('https://mail.google.com/mail/u/0/?pli=1#inb\
ox', 'Входящие (567) - palka280617@gmail.com - Gmail', '2020-11-02', '1\
4:25:46.480694', 0)], '2020-11-12'))
    set()
    """

    result = set()
    lenth = len(visits)
    for i in range(lenth):
        if date == visits[i][2]:
            result.add(visits[i][0])
    return result


def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites

    >>> print(most_frequent_sites([('https://mail.google.com/mail/u/0/?pli=1#inb\
ox', 'Входящие (567) - palka280617@gmail.com - Gmail', '2020-11-02', '1\
4:25:46.480694', 0)], 2))
    {'https://mail.google.com/mail/u/0/?pli=1#inbox'}
    """
    result = set()
    set_of_urls = dict()
    visits_lenth = len(visits)
    for i in range(visits_lenth):
        if visits[i][0] in set_of_urls:
            set_of_urls[visits[i][0]] += 1
        else:
            set_of_urls[visits[i][0]] = 1
    list_urls = list(set_of_urls.items())
    list_urls.sort(key=lambda i: i[1])
    list_urls.reverse()
    if number < len(list_urls) - 1:
        for i in range(number):
            result.add(list_urls[i][0])
    else:
        lenth = len(list_urls)
        for i in range(lenth):
            result.add(list_urls[i][0])
    return result


def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)

    >>> print(get_url_info([('https://mail.google.com/mail/u/0/?pli=1#inbox', 'Вхо\
дящие (567) - palka280617@gmail.com - Gmail', '2020-12-30', '14:25:46.480694', 2\
1)], 'https://mail.google.com/mail/u/0/?pli=1#inbox'))
    ('Входящие (567) - palka280617@gmail.com - Gmail', '2020-12-30', '14:25:46.480694', 1, 21.0)
    """
    num_of_visits = 0
    last_visit_date = ''
    last_visit_time = ''
    average_time = 0
    title = ''
    for i in visits:
        if i[0] == url:
            num_of_visits += 1
            if last_visit_date < i[2]:
                last_visit_date = i[2]
            if last_visit_time < i[3]:
                last_visit_time = i[3]
            title = i[1]
            average_time += i[4]
    try:
        average_time /= num_of_visits
    except ZeroDivisionError:
        average_time = 0
    result = (title, last_visit_date, last_visit_time,
              num_of_visits, average_time)
    return result
