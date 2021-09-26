x = input()
y = "0" + x
lenth = len(x)
number = ""
print(x)
print(y)
for i in range(lenth):
    number += str(int(y[i]) ^ int(x[i]))
print(number)