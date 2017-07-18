#term_cond.py
import sys


n = int(input("number: "))

factor = 2
old_factor = 0
#while factor*factor <= n:
while factor <= n
	while (n % factor) == 0:
		# Cast out and write factor
		n //= factor
		if factor != old_factor:
			print(str(factor) + " ")
			old_factor = factor

	factor += 1

if n > 1:
	print(n)
print(" ")	

  #i <= n instead of i*i <= n
  # write the same result
  # python factor2.py
#number: 200
#2
#5

