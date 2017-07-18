#wind chill 2
#-45oF to +45oF and wind speeds 3 to 60 mph
T = float(input("Temperature: "))
 


if T < -45 or  T > 45:
	print("T has to be more than -45 and less than +45")

W = float(input("Wind speed: "))

if W < 3 or W > 60:
	print("W has to be more than 3 or less than 61")

w_chill = 35.74 + 0.6215 * T + (0.4275 * T - 35.75) * (v ** 0.16)

print(w_chill)