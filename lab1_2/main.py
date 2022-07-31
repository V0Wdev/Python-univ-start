import math

a = 0.5
x = 0.34
l = 1.65

y = (math.sin(3*l) + (x**2 + 1) * ((math.cos(l))**2)*x - 0.8 * (10**(-2*a))*math.exp(x))/((x+1)**(1/3) - math.log10((a**2)*x) + 0.3*(x**3 - a) + math.acos(x))
print(y)
