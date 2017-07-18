#calculations
import math

P = 1000
R = 0.05
T = 5

A = P * math.e ** (R * T)


base_money_per_year = P/T


print("base money per year " , base_money_per_year)

interest_per_year = A - P

print("interest per year " , interest_per_year)


money_with_interest_per_year = interest_per_year + P

print("money with interest per year " , money_with_interest_per_year) 

print("Compunded interest " , A)