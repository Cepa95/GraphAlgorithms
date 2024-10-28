def unique_elements(firstList, secondList):
    return list(set(firstList + secondList))


firstList = [1, 2, 3, 4, 5]
secondList = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]


print(type(unique_elements(firstList, secondList)))
print(unique_elements(firstList, secondList))


