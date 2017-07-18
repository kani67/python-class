import sys

n = int(input("number: "))

factor = 2

while factor*factor <= n:
	while (n % factor) == 0:
		# Cast out and write factor
		n //= factor
		print(str(factor) + " ")

	factor += 1

if n > 1:
	print(n)
print(" ")	
