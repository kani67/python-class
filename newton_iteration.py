#newton's method iteration

#x*n+1 = x*n - f(x*n) / f'(x*n)
#f(x) = x**2 - 0.5
#f'(x) = 2x
guesses = int(input("How many guesses? "))
x = 3
d = 2 * x
n = 10

root_list = []
guess = x - (x**2 - n) / d

for i in range(0, guesses):
	closer_guess = guess - (guess**2 - n) / d
	root_list.append(closer_guess)
	guess = closer_guess

print(root_list)	