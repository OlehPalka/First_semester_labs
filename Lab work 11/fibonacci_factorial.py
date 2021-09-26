"""
this module countes fibonacci numbers and
factorial using recursion and iteration.
"""


import functools
import time


def factorial_recursive(number, verbose=False):
    """
    This function counts factorial using recursion.

    >>> print(factorial_recursive(5))
    120
    """
    if verbose:  # verbose parametr
        print(f'factorial_recursive({number})')
    if number == 1:  # recursive func
        return number
    return factorial_recursive(number-1, verbose=verbose) * number


def factorial_iterative(number, verbose=False):
    """
    This function returns factorial of the number using iteration.

    >>> factorial_iterative(5)
    120
    """
    if verbose:  # verbose parametr
        print(f'factorial_iterative({number})')
    result = 1
    for num in range(number):  # iteration to find factorial
        result *= (num + 1)
    return result


@functools.lru_cache(1000)
def fibonacci_recursive(number, verbose=False):
    """
    This function returns fibonacci number for n.
    This function use recursion.

    >>> fibonacci_recursive(1)
    1
    """
    if verbose:  # verbose parametr
        print(f'fibonacci_recursive({number})')
    if number < 2:  # recursive func
        return 1
    result = fibonacci_recursive(
        number - 1, verbose=verbose) + fibonacci_recursive(number - 2, verbose=verbose)
    return result


def fibonacci_iterative(number, verbose=False):
    """
    This function returns fibonacci number for n.
    This function use iteration.

    >>> fibonacci_recursive(1)
    1
    """
    if verbose:  # verbose parametr
        print(f'fibonacci_iterative({number})')
    beggining = [1, 1]  # start list for fibonacci numbers
    for index in range(number - 1):  # iteration to find fib nums
        beggining.append(beggining[index] + beggining[index + 1])
    return beggining[-1]


def numbers_time_test(function=0, realisation=0, verbose=True):
    """
    This function returns time of completing the fucntion, and if verbose == True,
    prints number of recurtions and the result of function.
    Also user enteres number meaning for function.
    """
    # нормальний варік:
    # function = {(0, 0): factorial_recursive(number), (0, 1): factorial_iterative(number)...}
    number = int(input())
    if function == 0 and realisation == 0:
        start = time.time()
        result = factorial_recursive(number)
        if verbose:  # verbose parametr
            print(f"Number of recursions is {number}")
            print(result)
        func_result = time.time() - start
    elif function == 0 and realisation == 1:
        start = time.time()
        result = factorial_iterative(number)
        if verbose:  # verbose parametr
            print(result)
        func_result = time.time() - start
    elif function == 1 and realisation == 0:
        start = time.time()
        result = fibonacci_recursive(number)
        if verbose:  # verbose parametr
            print(f"Number of recursions is {number}")
            print(result)
        func_result = time.time() - start
    elif function == 1 and realisation == 1:
        start = time.time()
        result = fibonacci_iterative(number)
        if verbose:  # verbose parametr
            print(result)
        func_result = time.time() - start
    return func_result
