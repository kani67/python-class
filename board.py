#board.py

n = int(input("Size of square: "))

for i in range(1, n+1):
	
	
	
	if i % 2 == 0:
		print("", n * "*")
	else:
		print(n * "*")	