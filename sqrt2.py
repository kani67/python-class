#sqrt2.py

import sys, math


EPSILON = float(sys.float_info.epsilon)

c = float(input(" value:  "))
t = c
d = c * 0.5

while abs(t - c / t) > (EPSILON * t):
    t = 0.5 *( d + c / d)
    print(t)    
print("final t" , t)    