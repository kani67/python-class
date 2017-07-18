

n = int(input("Value "))

i= 1

while i <= n:
	j = 1
	while j <= n:
		if (i % j == 0 ) or (j % i == 0):
			print("* " , end = "")
		else:
			print(" " , end = " ")	
	
		j += 1		

	print(i)
	i += 1	