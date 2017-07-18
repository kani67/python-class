#gambler3.py
import random
import sys

stake = int(input("Stake: "))
goal = int(input("Goal: "))
bets = int(input('How much do you want to bet?: '))
wins = 0

for t in range(nbet):
	# Run one experiment
	cash = stake
	for c in range (cash > 0 , goal):
	#while (cash > 0) and (cash < goal):
		#Simulate one bet


		bets += 1
		for m in (1, cash):
			for k in (1, cash):
				print("* ", end = " ")

		print("", end="")


		if random.randrange(0, 2) == 0:
			cash += 1
		else:
			cash -= 1

	if cash == goal:
		wins += 1

print(str(100 * wins // nbet) + "% wins")	
print("Avg # bets: " + str(bets // nbet))
