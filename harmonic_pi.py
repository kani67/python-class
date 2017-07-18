#harmonic_pi.py

#the sum 1/12 + 1/22 + ... + 1/n2 does converge to a constant as n grows to infinity.
#(Indeed, the constant is π2/6, so this formula can be used to estimate the value of π.)
#Which of the following for loops computes this sum? 
#Assume that n is the integer 1000000 and total is a float initialized to 0.0.
import math

total = float(0.0)
n = 1000000
for i in range(1, n+1):
	total += 1 / (i*i)
#total = 1.64493306684877

#for i in range(1, n+1):
#    total += 1.0 / i*i

#total = 1000000.0

#for i in range(1, n+1):
#   total += 1.0 / (i*i)
 
#total = 1.6449240668982423

#for i in range(1, n+1):
#    total += 1.0 / (1.0*i*i)

#total = 1.6449240668982423
constant = math.pi**2 / 6
#constant = 1.6449240668982423
print(constant)
print(total)