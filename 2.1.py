import numpy as np
def countDifferentElements(array):
    count = 0
    while array:
        current = array.pop(0)
        if current in array:
            for element in array:
                if element == current:
                    array.remove(element)
        else:
            count+=1
    return count

def buildArray():
    B = []
    A = [[1,2,3,1],
        [9,9,2,2],
        [1,1,2,3],
        [3,2,2,1]]

    for row in A:
        B.append(countDifferentElements(row))
    print(B)

buildArray()


