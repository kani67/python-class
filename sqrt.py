import sys, math


EPSILON = float(sys.float_info.epsilon)

c = float(input(" value:  "))
t = c
while abs(t - c / t) > (EPSILON * t):
    # Replace t by the average of t and c/t.
    t = (c / t + t) / 2.0
print(t)    