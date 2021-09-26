import math
x = int(input())
y = x // 7
denominator = (7 ** y) * math.factorial(y)
result = math.factorial(x) / denominator
print(int(result))