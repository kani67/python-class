#ntable.py

n = int(input("table size: "))

for i in range(1,n+1):
	#print("*", end=" ")

	for j in range(1,n+1):
		
		while i != j:

			while i > j:
				k = i - j
				i = k

			while j > i:
				k = j - i
				j = k

		if i == 1 and j ==1:

			print("* ", end = " ")
	
		else:
			print(" ", end = " ")	



