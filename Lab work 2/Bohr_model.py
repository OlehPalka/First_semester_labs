# R**2 =(n^2*h^2*4*math.pi*є*є0*R)/(4*math.pi^2*m*e^2)
# R - ? radius
# n - (input) elctrical_condition_number
# h = planck_constant = 6.62607015e-34 J Hz^-1
# m = electron_mass = 9.1093837015e-31 kg
# є = dielectric_constant = 1
# є0 = electic_constant = 8.8541878128e-12
# e = зряд елктрона = electron_charge = 1.602176634e-19
# скорочена формула R=(n^2*h^2*є*є0)/(math.pi*m*e^2)
import math
elctrical_condition_number = float(input())
planck_constant = 6.62607015e-34
electron_mass = 9.1093837015e-31
dielectric_constant = 1
electic_constant = 8.8541878128e-12
electron_charge = 1.602176634e-19
# обчислюю чисельник
numerator = elctrical_condition_number**2 * planck_constant**2 * dielectric_constant * electic_constant 
# обчислюю знаменник
denominator = math.pi * electron_mass * electron_charge**2
# обчислюю радіус
radius = numerator / denominator
# виводжу радіус
print(float('{:.5g}'.format(radius)))