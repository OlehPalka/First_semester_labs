x = int(input())
y = int(input())
num_of_repeats = y
m = 0
a = y
n = y
for i in range(y):
    for i in range(num_of_repeats):
        if m == 0:
            print((x + m), end = "")
        else:
            print("",(x + m), end = "")
        m += 1 
    m = 0
    n -= 1
    num_of_repeats -= 1
    print()