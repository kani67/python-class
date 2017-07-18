#test_ntable.py
from fractions import gcd

n = int(input("table size: "))

for i in range(1,n+1):
	
	a = i
	for j in range(1,n+1):
		b = j
		r = gcd(a,b)
		
		if r == 1:
			print("* ", end =" ")	
		else:
			print(" ", end=" ")	
	print("")			