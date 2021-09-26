import sys


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
list_of_repnums = list("")

def return_digits(number):
    """
    str -> str
    This function returns big number (each meaning of big number is printed by
    meaning from input number)
    >>> return_digits("123") # doctest: +ELLIPSIS
    ' 1...333 '
    """
    try:
        digits = number
        row = 0
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                digit[row] = digit[row].replace("*", str(number))
                line += digit[row]
                column += 1
            list_of_repnums.append("\n" + line)
            row += 1
        result = "".join(list_of_repnums)
        return result[1:]
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", Digits[sys.argv[1]])

try:
    print(return_digits(sys.argv[1]))
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", Digits[sys.argv[1]])
