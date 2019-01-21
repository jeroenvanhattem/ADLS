"""
Jeroen van Hattem
1675180
TICT-TI-V2A
Joop Kaldeway
"""
import random

"""
Description
The birthdayChances() function will calculate the chance of two people in a group of 23 sharing their birthday.

Return
------
chance: int
The chance two people share their birthday
"""
def birthdayChances():
    count = 0
    birthday = False

    for i in range(100):
        birthdays = []
        for i in range(23):
            birthdays.append(random.randint(1, 365))

        for x in range(len(birthdays)):
            for y in range(len(birthdays)):
                birthday = False
                if x != y:
                    if birthdays[x] == birthdays[y]:
                        birthday = True
            if birthday:
                count += 1
                birthday = False

    return count

print("Times: ", birthdayChances())