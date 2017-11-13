import random

"""
description
The birthdayChances() function will calculate the chance of two people in a group of 23 sharing their birthday.

Return
------
chance: int
The chance two people share their birthday
"""



def birthdayChances():
	count = 0

	for i in range(100):
		birthdays = []
		for i in range(23):
			birthdays.append(random.randint(1, 365))

		for x in range(len(birthdays)):
			for y in range(len(birthdays)):
				if x != y:
					if birthdays[x] == birthdays[y]:
						count += 1;


	return count

print("Aantal keer: ", birthdayChances())