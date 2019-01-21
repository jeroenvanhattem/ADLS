"""
Jeroen van Hattem
1675180
TICT-TI-V2A
Joop Kaldeway
"""

"""
description
The getNumbers(a) function will seperate numbers from letters within a string. These numbers will be returned in a list.
----------
a : list
A string containing letters and numbers.

Return
------
b: list
A list that contains the extracted numbers from list A
"""

a = 'een123zin45 6met-632meerdere+7777getallen'


def getNumbers(a):
    length = len(a)
    temp = []
    b = []
    for x in a:
        if x.isdigit():
            temp.append(int(x))
        else:
            if len(temp) != 0:
                number = 0
                for y in temp:
                    if number == 0:
                        number = y
                    else:
                        number = number * 10 + y
                        print(number)
                b.append(number)
                temp = []
    return b


print(getNumbers(a))
