__author__ = "miha_focsa"

import random

licenses = 0

def trial():
	d1 = random.randint(100, 366)
	d2 = random.randint(0, 366)
	d3 = random.randint(0, 366)
	d4 = random.randint(95, 99)
	d5 = 0
	d6 = random.randint(0, 9)
	d7 = random.randint(0, 9)
	d8 = random.randint(0, 9)
	d9 = random.randint(0, 9)
	d10 = random.randint(0, 9)
	d11 = random.randint(0, 9)
	d12 = random.randint(0, 9)
	d13 = random.randint(0, 9)
	d14 = random.randint(0, 9)
	d15 = random.randint(0, 9)
	d16 = random.randint(0, 9)
	
	z = int(str(d5) + str(d6) + str(d7) + str(d8) + str(d9) + str(d10) + str(d11))
	

	if int(z) % 7 == 0:
		if not d16 == 0 and not d16 == 8 and not d16 == 9:
			print(f"{d1}{d4}-OEM-{d5}{d6}{d7}{d8}{d9}{d10}{d11}-{d12}{d13}{d14}{d15}{d16}")
			global licenses
			licenses += 1
		else:
			foundlicense = False
	else:
		foundlicense = False

numlicenses = int(input(f"Program made by {__author__}. How many licenses do you want? : "))


while licenses != numlicenses:
	trial()





