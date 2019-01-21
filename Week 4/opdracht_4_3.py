"""
Jeroen van Hattem
1675180
TICT-TI-V2A
Joop Kaldeway
"""
"""
Definition
    Calculate the pascal triangle up to N

Parameters
----------
N : int
    Max value of the triangle

Return
------
value : list
    Return the triangle
"""
def pascalTriangle(N):
    if n == 0:
        print("Not legit")
    elif n == 1:
        return [[1]]
    else:
        newRow = [1]
        result = pascalTriangle(n - 1)
        endRow = result[-1]
        lengthEndRow = len( endRow ) - 1
        for i in range( lengthEndRow ):
            newRow.append(endRow[i] + endRow[i + 1])
        newRow += [1]
        result.append(newRow)

    return result

def B(n, k=0):
    result = pascalTriangle(n+1)
    return result[n][k]


d = B(100,50)
print ( d )

