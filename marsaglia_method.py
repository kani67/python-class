#marsaglia_method.py
import math, random
x = 1.0
y = 1.0

while x*x + y*y >= 1.0:

	x = -1.0 + 2.0*random.random()
	y = -1.0 + 2.0*random.random()

	#if x*x + y*y <= 1.0:
	#	break

a = 2 * x * math.sqrt(1 - x*x - y*y) 
b = 2 * math.sqrt(1 - x*x - y*y)
c = 1 - 2*(x*x + y*y)

print(a, b, c)