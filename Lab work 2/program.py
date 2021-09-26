import math


def sales_prediction():
    g = float(input()) 
    a = (g / 100) * 23 + g
    print(a)   


def pound_to_kilogram():
    x = float(input())
    a = (x * 0.454) * 1000
    b = x * 0.454
    c = (x * 0.454) / 1000
    print(a)
    print(b)
    print(c)
 
    


def cashier():
    price_1 = float(input())
    price_2 = float(input())
    price_3 = float(input())
    price_4 = float(input())
    price_5 = float(input())
    a = price_1 + price_2 + price_3 + price_4 + price_5
    b = (a / 100) * 7
    c = a + b
    print(int(a))
    print(round(b, 2))
    print(c)



def odometer():
    speed = float(input())
    time = float(input())
    distance = speed * time
    print(int(distance))


def payment_instalments():
    money = float(input())
    payments_amount = float(input())
    overal_money = (money / 100) * 105
    one_payment = overal_money / payments_amount
    print(overal_money)
    print(one_payment)


def miles_per_galon():
    miles = float(input())
    galons_of_fuel = float(input())
    MPG = miles / galons_of_fuel
    print(MPG)



def cookie():
    amount_of_cookies = int(input())
    coeficient = amount_of_cookies / 48
    print(1.5 * coeficient)
    print(1 * coeficient)
    print(2.75 * coeficient)



def vineyard():
    line_lenth = float(input())
    lenth_used_by_stick = float(input())
    lenth_between_grapes = float(input())
    amount_of_trees = (line_lenth - 2 * lenth_used_by_stick) / lenth_between_grapes
    print(math.floor(amount_of_trees))
    


def compound_interest():
    P = float(input())
    r = float(input())
    n = float(input())
    t = float(input())
    A = P * (1 + (r / 100) / n)**(n * t)
    print(A)


if __name__ == "__main__":
    eval(input() + "()")