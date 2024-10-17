def printNumberTriangle(n):
    if n > 20:
        return
    for i in range(1, n + 1):
        for j in range(i * 2 - 1):
            if j < i:
                print((i + j) % 10, end=" ")
            else:
                print((i + 2 * i - j - 2) % 10, end=" ")
        print()  


n = 9
printNumberTriangle(n)
