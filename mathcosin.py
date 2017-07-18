import math


angle = float(input("Angle? "))



result = (math.cos(angle) *  math.cos(angle)) +  (math.sin(angle) * math.sin(angle))

if result == 1.0:
    print(result)
else:
    print("not 1.0" , result)    