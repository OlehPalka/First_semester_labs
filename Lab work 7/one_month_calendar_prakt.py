

def weekday_name(number: int) -> str:
    """
    int -> str
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    >>> weekday_name(8)

    """
    if number < 0 or number > 6:
        return None
    else:
        Week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        x = Week_days[number]
    return x
import doctest
print(doctest.testmod())
	
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
    pass