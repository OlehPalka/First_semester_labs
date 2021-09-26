import math
# ввід даних
x = input()
x = float(x)
# переводжу градуси в радіани
math.radians(x)
# шукаю і друкую синус
print("SIN =", f'{math.sinh(x):.4f}')
math.exp(x)
# шукаю і виводжу EXP
print("EXP =", f'{1/2 * (math.exp(x) - math.exp(x * (-1))):.4f}')
# шукаю і виводжу формулу з е 
print("E =", f'{1/2 * (math.e**x - math.e**(x * (-1))):.4f}')