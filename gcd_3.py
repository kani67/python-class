#gcd_3.py
a = 15
b = 8



while a != b:
     while a > b:
     	c = a - b
     	a = c
     
     while b > a:
         c = b - a
         b = c
     
print(a, b, c) 