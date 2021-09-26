x = int(input())
y = int(input())
if x == 1:
    print("*")
else:
    for i in range(1):
        print(y * "*")
    for i in range(x - 2):
        print(("*{}*").format(" " * (y - 2)))
    for i in range(1):
        print(y * "*")    