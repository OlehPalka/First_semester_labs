"""
This module makes operations with functions.
"""


def find_max_1(function, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    result = ""
    for x_mean in points:
        if isinstance(function, str):
            func_result = eval(function, {"x": x_mean})  # count str function
        else:
            func_result = function(x_mean)  # count lambda function
        if result == "":  # create a result
            result = func_result
        else:
            if result < func_result:
                result = func_result
    return result


def find_max_2(function, points):
    """
    (function or str, list(number)) -> (list())

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    result = list()
    for x_mean in points:
        if isinstance(function, str):
            func_result = eval(function, {"x": x_mean})  # count str function
        else:
            func_result = function(x_mean)  # count lambda function
        if result == []:
            result = [func_result, [x_mean]]
        else:
            if result[0] <= func_result:  # check for other max points
                if result[1][0] != x_mean and result[0] == func_result:
                    result[1].append(x_mean)
                else:
                    result = [func_result, [x_mean]]
    return result[1]


def compute_limit(seq):
    """
    (function or str) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []  # the list sequence elements
    i = 0
    while True:
        n_mean = 10 ** i  # the number of element
        if isinstance(seq, str):
            lst.append(eval(seq, {"n": n_mean}))  # adding new element
        else:
            lst.append(seq(n_mean))
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return round(lst[i], 2)
        i += 1


def compute_derivative(function, x_0):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    aprox = []
    i = 0
    while True:
        d_from_x = 10 ** -i
        x_mean = x_0 + d_from_x
        if isinstance(function, str):
            d_from_function = eval(function, {"x": x_mean})  # dF = f(x_0 + dx)
        else:
            d_from_function = function(x_mean)
        x_mean = x_0
        if isinstance(function, str):
            # dF = f(x_0 + dx) - f(x_0)
            d_from_function -= eval(function, {"x": x_mean})
        else:
            d_from_function -= function(x_mean)
        der = d_from_function / d_from_x  # der = (f(x_0 + dx) - f(x_0))/ dx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return round(aprox[i], 2)
        i += 1


def get_tangent(function, x_0):
    """
    (function or str, number) -> (number)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '-3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '-3.0 * x + 4.0'
    """
    derivative = compute_derivative(function, x_0)  # k
    x_mean = x_0
    if isinstance(function, str):
        f_x_0 = eval(function, {"x": x_mean})
    else:
        f_x_0 = function(x_0)
    the_last_part = derivative * - x_0 + f_x_0  # b
    if the_last_part > 0:  # check for plus or minus before "b"
        plus_minus = ' + '
    else:
        the_last_part = the_last_part * -1
        plus_minus = ' - '
    return str(derivative) + ' * x' + plus_minus + str(the_last_part)


def get_root(function, low_limit, high_limit):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    x_mean = low_limit + 0.001
    root = None
    while True:
        if isinstance(function, str):
            result = eval(function, {"x": x_mean})  # count str function
        else:
            result = function(x_mean)  # count lambda function
        if round(result, 2) == 0:  # check in which x function = 0
            root = round(x_mean, 2)
        x_mean += 0.001
        x_mean = round(x_mean, 3)
        if x_mean == high_limit:
            break
    return root
