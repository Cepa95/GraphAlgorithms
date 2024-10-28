def findBiggestNumber(lst):
    biggestNumberValue = None

    for i in range(len(lst)):
        if isinstance(lst[i], (int, float)):
            if biggestNumberValue is None:
                biggestNumberValue = lst[i]
            elif lst[i] > biggestNumberValue:
                biggestNumberValue = lst[i]

    return biggestNumberValue


lst = [7, 18, 3, "a", True, (2, 3)]
print(findBiggestNumber(lst))


def findBiggestNumberRecursive(lst, index=0, biggestNumberValue=None):
    if index >= len(lst):
        return biggestNumberValue

    if isinstance(lst[index], (int, float)):
        if biggestNumberValue is None or lst[index] > biggestNumberValue:
            biggestNumberValue = lst[index]

    return findBiggestNumberRecursive(lst, index + 1, biggestNumberValue)


lst = [7, 18, 3, "a", True, (2, 3)]
print(findBiggestNumberRecursive(lst))
