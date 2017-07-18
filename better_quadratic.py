#-----------------------------------------------------------------------
# quadratic.py
#-----------------------------------------------------------------------

import sys
import math

# Accept floats b and c as command-line arguments.

#write the roots of the polynomial ax2bx + c, 
#write an appropriate error message 
#if the discriminant is negative, 
#and behaves appropriately (avoiding division by zero) 
#if a is zero.

a = float(input("Value a: "))
b = float(input("Value b: "))
c = float(input("Value c: "))



#ax**2 + b*x + c
#find x in the equation ax**2 + b*x + c

square_root1 = -b + (math.sqrt(b**2 - (4 * a * c)))
square_root2 = -b - (math.sqrt(b**2 - (4 * a * c)))

print(square_root1)
print(square_root2)
divisor = 2 * a

x1_is = float(square_root1 / divisor)
x2_is = float(square_root2 / divisor)
#print(x1_is, x2_is)

#-----------------------------------------------------------------------

# better_quadratic.py -3.0 2.0
# 2.0
# 1.0

# quadratic.py -1.0 -1.0
# 1.618033988749895
# -0.6180339887498949

# quadratic.py 1.0 1.0
# Traceback (most recent call last):
#   File "quadratic.py", line 17, in <module>
#     d = math.sqrt(discriminant)
# ValueError: math domain error
