#testing while and for loops
n = 4
a = 0
b = 0
c = 0
d = 0
for for_i in range(1, n + 1):
	for for_j in range(1, n + 1):
		a +=1
		print("for j loop " , a)
	b += 1		
	print("for i loop " ,b)

while_i = 1

print("*************************")
while while_i < n+1:
	while_j = 1
	while while_j < n+1:
		while_j += 1
		c +=1  
		print("while j loop " ,c)
	d +=1	
	print("while i loop " ,d)
	while_i += 1		
		
	