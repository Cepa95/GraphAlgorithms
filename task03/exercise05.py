def invertDictionary(d):
    newDict = {}
    for key in d:
        for value in d[key]:
            if value not in newDict:
                newDict[value] = []
            newDict[value].append(key)
    return newDict


d = {1: [2, 3, 5], 2: [1, 4], 3: [1, 2]}
newDict = invertDictionary(d)

for key in sorted(newDict):
    print(f"{key}: {newDict[key]}")
