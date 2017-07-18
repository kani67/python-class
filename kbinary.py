#kbinary

import sys

i = int(input("Number i "))
k = int(input("base k "))


#Convert a positive number i to its digit representation in base k.
digits = []
while i > 0:
	digits.insert(0, i % k)
	i  = i // k
    



#Compute the number given by digits in base k.
index = 0
for d in digits:
	index = k * index + d
    

print("to digits ", digits)
print("from digits ", index)    