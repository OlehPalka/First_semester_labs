import math
def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    This function accepts 8 numbers (each of them is whole or with float point;
     k1 = k3 if lines are parallel), which presente 4 lines equations.
     Function has to return area of quadrangle (number rounded to two meanings
     after coma).
    >>> four_lines_area(1, 1, 2, 14, 34, 3, 9, 0.5)
    86.27
    >>> four_lines_area(12, 43, 2, 54, 34, 27, 9, 0.5)
    297.44
    >>> four_lines_area(1, 6, 1, 8, 34, 56, 3, 5)
    None
     """
    tochka_1 = lines_intersection(k1, c1, k2, c2)
    if k1 == k2: #check if two lines are not parallel
        area = None
        return area
    tochka_2 = lines_intersection(k2, c2, k3, c3)
    if k2 == k3:
        area = None
        return area
    tochka_3 = lines_intersection(k3, c3, k4, c4)
    if k3 == k4:
        area = None
        return area
    tochka_4 = lines_intersection(k4, c4, k1, c1)
    if k4 == k1:
        area = None
        return area
    tuple_of_distances = all_lines_distance(tochka_1, tochka_2, tochka_3,
    tochka_4) #
    area = quadrangle_area(tuple_of_distances[0], tuple_of_distances[1],
    tuple_of_distances[2], tuple_of_distances[3], tuple_of_distances[4],
    tuple_of_distances[5])
    return area

def lines_intersection(k1, c1, k2, c2): #here i find lines intersection point
    """
    (int or float, int or float, int or float, int or float) -> float
     This function accepts 4 numbers (every number is whole or with floating
     point), and returns tuple of two numbers with float point - meanings of
     (x,y), which are crossing points of two lines (numbers are rounded to
     two means after point).
    If lines are parallel, or are identical, function should return None.

    >>> lines_intersection(1, 2, 1, 7)
    None
    >>> lines_intersection(1, 2, 1, 2)
    None
    >>> lines_intersection(1, 4, 2, 7)
    (-3.0, 1.0)
    >>> lines_intersection(1.34, 4.865, 2.0, 7.35)
    (-3.77, -0.18)
    """
    if k1 == k2: #check if two lines are not parallel
        x1_y1_kortezh = None
    elif k1 != k2: #here i find x and y meanings
        x = (c2 - c1) / (k1 - k2)
        y = (k1 * x + c1)
        x = round(x, 2)
        y = round(y, 2)
        x1_y1_kortezh = (x, y) #write x and y down into the tuple
    return x1_y1_kortezh

def distance(x1, y1, x2, y2): #here i find distance between two points
    """
    (int or float, int or float, int or float, int or float) -> float
    This function accepts 4 numbers (each is whole or with float pooint),
     which are coordinates of two points. Function returns distance between
     theese two points (float number rounded to two meanings after coma).

    >>> distance(2, 4, 6, 8)
    5.66
    >>> distance(43, 2, 18, 13)
    27.31
    >>> distance(43.34, 2.56, 18.578, 13.2)
    26.95
    """
    segment_distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    #formula of finding distance
    return segment_distance


def all_lines_distance(tochka_1, tochka_2, tochka_3, tochka_4):
    # here i write down all qadrangle distances into one tuple
    """
    (tuple, tuple, tuple, tuple) -> tuple
    This function accepts 4 points. It enters all meanings of quadrangle
    distances to another tuple.
    >>> all_lines_distance((1.1, 56.2), (0.84, 55.69), (-1.06, -9.04),
    (-14.17, -127.0))
    (0.57, 64.76, 118.69, 183.84, 65.28, 183.31)
    """
    AB_distance = distance(tochka_1[0], tochka_1[1], tochka_2[0], tochka_2[1])
    BC_distance = distance(tochka_2[0], tochka_2[1], tochka_3[0], tochka_3[1])
    CD_distance = distance(tochka_3[0], tochka_3[1], tochka_4[0], tochka_4[1])
    DA_distance = distance(tochka_4[0], tochka_4[1], tochka_1[0], tochka_1[1])
    CA_distance = distance(tochka_1[0], tochka_1[1], tochka_3[0], tochka_3[1])
    BD_distance = distance(tochka_2[0], tochka_2[1], tochka_4[0], tochka_4[1])
    alllines_distance = (AB_distance, BC_distance, CD_distance, DA_distance,
    CA_distance, BD_distance)
    return alllines_distance
    
def quadrangle_area(AB, BC, CD, DA, AC, BD):
# Here i find the area of the quadrangle set bi the lines i have counted before
    """
    (float, float, float, float, float, float) -> float
    This function accepts 6 numbers (each of them is whole or with float point),
     which present lenth of quadrangle sides and diagonals and returns area
     of this quadrangle (number rounded to two meanings after coma).
     If there is no such quadrangle, function returns None.
    >>> quadrangle_area(1000, 10000, 10000, 1000, 1, 1)
    None
    >>> quadrangle_area(3, 4, 3, 4, 5, 5)
    12
    """
    area_number = (4 * (AC ** 2) * (BD ** 2) - (BC ** 2 + DA ** 2 - AB ** 2
    - CD ** 2) ** 2) / 16
    # This is the formula of the quadrangle area

    if area_number > 0: #here i exclude -area
        area = round((math.sqrt(area_number)), 2)
        return area

    return None
