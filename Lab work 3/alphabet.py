alfabet = ["A", "B", "C", "D", "E", "F", "G", "H",
 "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
  "S", "T", "U", "V", "W", "X", "Y", "Z"]
x = int(input())
n = 0
m = 1
if x == 1:
    a = 1
elif x == 2 or x == 3:
    a = 2
elif x == 4 or x == 5 or x == 6:
    a = 3
elif x == 7 or x == 8 or x == 9 or x == 10:
    a = 4
elif x == 11 or x == 12 or x == 13 or x == 14 or x == 15:
    a = 5
elif x == 16 or x == 17 or x == 18 or x == 19 or x == 20 or x == 21:
    a = 6
else:
    a = 7
for i in range(a):
    print((a - m) * "  ", end = "")
    list_of_tries = list(range(0, m))
    for i in (list_of_tries):
        if n == 0 or n == 1 or n == 3 or n == 6 or n == 10 or n == 15 or n == 21:
            print(alfabet[n], end = "")
        else:
            print("",alfabet[n], end = "")
        n += 1
        if n == x:
            break
    m += 1
    print()