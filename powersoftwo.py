import sys

n = int(input("Power of 2 "))
power = 1
i = 0
while i <= n:
    print(str(i) + " " + str(power))
    power = power * 2
    i = i + 1