
T = float(input("Temperature: "))
v = float(input("Wind speed: "))

w = 35.74 + 0.6215 * T + (0.4275 * T - 35.75) * (v ** 0.16)

print(w)