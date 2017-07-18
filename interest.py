import math

P = 0
r = 0
t = 0

p = float(input("Amount invested: "))
r = float(input("Interest: "))
t = float(input("Time in years: "))

annual_interest = float(p * t * (r/100))

money = float(annual_interest + p)

print(money)