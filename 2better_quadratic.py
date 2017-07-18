import math

#find x in the equation ax**2 + b*x + c

a = float(input("Value a? "))
b = float(input("Value b? "))
c = float(input("Value c? "))

if a == 0 or b == 0 or c == 0:
	print("Zero is not allowed")
else:	
	square_root = math.sqrt(b**2 - (4 * a * c))
	disc_pos = -b + square_root
	disc_neg = -b  - square_root

	divisor = 2*a

	if divisor != 0:
		result_pos = disc_pos / divisor
		result_neg = disc_neg / divisor
		print(result_pos, result_neg)
	else:
		print("You can't divide by zero!!")


