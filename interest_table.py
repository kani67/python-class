#interest_table
import math


p = float(input("Amount invested: "))
r = float(input("Interest: "))
t = float(input("Time in years: "))

i = 1
total_per_year = 0
balance = p


while i <= t:
	annual_interest = p * (r / 100)
	
	print('\tAnnual interest: ' ,annual_interest)

	balance = balance + annual_interest
	print('\tbalance ', balance, '\t' )
	i  += 1

total_interest = float(p * t * (r/100))
money = float(total_interest + p)

print("Total dollars: " ,money)
