def findIntersection(a, b, c, d):
    start = max(a, c)
    end = min(b, d)

    if start <= end:
        return (start, end)

    return None


firstInterval = float(input("[a, b]: a = "))
secondInterval = float(input("[a, b]: b = "))
thirdInterval = float(input("[c, d]: c = "))
fourthInterval = float(input("[c, d]: d = "))


intersection = findIntersection(
    firstInterval, secondInterval, thirdInterval, fourthInterval
)

if intersection:
    print([intersection[0], intersection[1]])
else:
    print("There is no intersection.")
