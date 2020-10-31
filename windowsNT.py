__author__ = 'miha_focsa'

import random

licenses = 0

def trial():
	d1 = random.randint(100, 999)
	d2 = random.randint(0, 9)
	d3 = random.randint(0, 9)
	d4 = random.randint(0, 9)
	d5 = random.randint(0, 9)
	d6 = random.randint(0, 9)
	d7 = random.randint(0, 9)
	d8 = random.randint(0, 9)


	z = int(str(d2) + str(d3) + str(d4) + str(d5) + str(d6) + str(d7) + str(d8))


	if int(z) % 7 == 0:
		
		if not z == 999 and not z == 888 and not z == 777 and not z == 666 and not z == 555 and not z == 444 and not z == 333:
			
			if not d8 == 8 and not d8 == 9 and not d8 == 0:
				print(f"{d1}-{d2}{d3}{d4}{d5}{d6}{d7}{d8}")
				global licenses
				licenses += 1

			else:
				foundlicense = False

		else:
			foundlicense = False
	else:
		foundlicense = False


numlicenses = int(input(f"Program made by {__author__}. How many licenses do you want? : "))

while numlicenses != licenses:
	trial()
				
