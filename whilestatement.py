import sys , math
n = int(input("value  "))

power = 1
#for i in range(n+1):
#    print(str(i) + " " + str(power))
#    power *= 2

#while 2*power <= n:
#    power *=2
#print(power)  

#total = 0
#for i in range(1, n + 1):
#    total += 1
#print(total)   
#product = 1

#for i in range(1, n + 1):
#    product += 1
#print(product)

#for i in range(1, n+1):
#    print(str(i) + " ")
#    print(2.0 * math.pi * i / n)  
  

ruler = "1"
print(ruler)
for i in range(2, n+1):
    ruler = ruler + " " + str(i) + " " + ruler
    print(ruler)     