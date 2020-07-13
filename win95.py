__author__ = 'ThatScode'

import random

def trial():

		d1 = random.randint(1, 9)
		d2 = random.randint(1, 9)
		d3 = random.randint(1, 9)
		d4 = random.randint(1, 9)
		d5 = random.randint(1, 9)
		d6 = random.randint(1, 9)
		d7 = random.randint(1, 9)
		d8 = random.randint(1, 9)
		d9 = random.randint(1, 9)
		d10 = random.randint(1, 9)
		z = int(str(d4) + str(d5) + str(d6) + str(d7) + str(d8) + str(d9) + str(d10))

	
		if int(z) % 7 == 0:
			if d4 + d5 + d6 + d7 + d8 + d9 + d10 == 21:
				print(f"{d1}{d2}{d3}-{d4}{d5}{d6}{d7}{d8}{d9}{d10}")
			
			else:
				b = 1

		else:
			a = 1


numtrials = int(input(f"Program made by {__author__}. How many trials do you want? : "))

for i in range(numtrials):
	trial()