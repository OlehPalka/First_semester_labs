#f(x,μ,σ)=(1/sqrt(2*math.pi*σ^2))*math.e^(-(x-μ)^2/2*σ^2)
import math
# вводжу дані
x = float(input())
μ = float(input())
σ = float(input())
first_part = 1 / (math.sqrt(2 * math.pi * (σ**2)))
second_part = math.e ** (-1 * ((x - μ)**2)/(2 * (σ**2)))
result = first_part * second_part
# виводжу дані 
print(f'{result:.10f}')