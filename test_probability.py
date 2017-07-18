#test_probability.py
import random

trials = 1000
c = 0
rate = 5

for i in range(1, trials):
	r = random.randrange(0, 5)


	if r == 0:
		c += 1
		p =  c / trials
		print("% ", p*100)





