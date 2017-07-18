#ruler function
n = int(input("Ruler "))
ruler = "1"
print(ruler)

for i in range(2 , n + 1):
	ruler = ruler + " " + str(i) + ruler
	print(ruler)
# if you enter 100 the ruler goes on forever!