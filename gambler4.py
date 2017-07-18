#gamble2.py
import random
import sys

stake = int(input("Stake: "))
goal = int(input("Goal: "))
nbet = int(input('Number of bets: '))
p = int(input("probability p in range 0 to p: "))
trials = int(input("Trials: "))
wins = 0
bets = 0

for t in range(trials):
	# Run one experiment
	cash = stake
	for c in range (cash > 0 , goal):
	
		bets += 1
		for m in (1, cash):
			for k in (1, cash):
				print("* ", end = " ")

		print("", end="")
	

		if random.randrange(0, p) == 0:
			cash += 1
		else:
			cash -= 1

	if cash == goal:
		wins += 1
	print(" ")	
		
print(str(100 * wins // trials) + "% wins")	
print("Avg # bets: " + str(bets // trials))
