#binary2.py

n = int(input("Number "))

if n == 0:
    print(0)
else:
    # Repeatedly divide by two, and form the remainders backwards.
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2

    print(s)