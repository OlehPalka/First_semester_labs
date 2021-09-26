# N1. V = 4/3*pi*(r^3) # A = 4*pi*(r^2)
import math
r = input()
# обчислюю об'єм
V = (4 / 3) * (math.pi) * (float(r)**3)
# обчислюю площу кулі
V = ('{:.3f}'.format(V))
A = 4 * math.pi * (float(r)**2)
A = ('{:.3f}'.format(A))
# виводжу на екран результати
print('V =', float(V))
print('A =', float(A))