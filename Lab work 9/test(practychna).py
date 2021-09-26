# product = 1
# lst_iterator = iter([1, 2, 4, 8])
# while True:
#     try:
#         product *= next(lst_iterator)
#     except StopIteration:
#         break
# print(product)

# МОДУЛЬ itertools

# import itertools
# x = itertools.product("ABCD", repeat=2)
# for i in x:
#     print(i)

# # gen1 = (x*x for x in range(3))
# # for i in gen1:
# #     print(i)

# names = {"Арман": "Василь", "Васмлмна": "Віктор", "Ольга": "Поважук"}
# print(names.sort(lambda key: names[0]))


# def male_detection(name):

#     print(len(name) <= 5)
#     return len(name) <= 5

#     # for i in names:
#     #     print(i, male_detection(i))


# def names_info(process):
#     return [process(name) for name in names]


# y = (lambda x: x ** 2 + x for x in [1, 2, 3, -1])
# for i in y:
#     print(i)
# f = '2x + 3 = 0'
# print(eval(f))

def get_root(function, low_limit, high_limit):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    x = low_limit
    if callable(function):
        value_in_a = round(function(x), 3)
    else:
        value_in_a = round(eval(function), 3)

    while low_limit < high_limit:
        x = low_limit
        if callable(function):
            if round(function(x), 3) > 0.0 and value_in_a < 0 or round(function(x), 3) < 0.0 and value_in_a > 0:
                return round(low_limit, 2)
        else:
            if round(eval(function), 3) > 0.0 and value_in_a < 0 or round(eval(function), 3) < 0.0 and value_in_a > 0:
                return round(low_limit, 2)

        low_limit += 0.001


print(get_root('x', -1, 0.1))
