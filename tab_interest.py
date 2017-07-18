#!compound interest
P = float(input('Principle amount: '))
I = float(input('Interest: '))
T = int(input('Years: '))

i = 0
#calculations
import math

R = I / 100

A = P * math.e ** (R * T)

compounded_calc = 0
compounded_interest = 0
base_money_per_year = P/T



interest_calc = A - P
interest_per_year = interest_calc / T


accu_interest = interest_calc + P
i = 1

print("Year ", '\t Interest rate' , '\t Invested money')
while i <= T:

	compounded_calc= interest_per_year + base_money_per_year
	compounded_interest += compounded_calc
	
	print(i, '\t',I , '\t        ', compounded_interest)
	
	i +=1




print("")
print("Compunded interest " , A)