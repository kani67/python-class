import random

N = int(input("Number "))
sum_x = 0
min_max_list = []

for i in range(0, N):
	x = random.random()
	print(x)
	sum_x = x + sum_x
	min_max_list.append(x)
	
average = sum_x / N
minimum = min(min_max_list)
maximum = max(min_max_list)

#minimum = float(min(n1, n2,n3, n4, n5))
#maximum = float(max(n1, n2,n3, n4, n5))
#print(n1 ,n2, n3 ,n4, n5)
print("Average ", average)
print("Minimum ", minimum)
print("Maximum " ,maximum)