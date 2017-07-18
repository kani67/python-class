#unit_disk.py
import random

x = -1.0 + 2.0*random.random()
y = -1.0 + 2.0*random.random()

while x*x + y*y <=1:
	x = -1.0 + 2.0*random.random()
	y = -1.0 + 2.0*random.random()
	
    

#    if x*x + y*y <= 1.0:
 #       break

#0.3120050051562737 -0.5702292871868662
print(x,y)