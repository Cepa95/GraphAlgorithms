def readMatrixFromFile(filename):
    file = open(filename, "r")
    # print(file.read())
    matrix = []
    for line in file:
        # row = list(map(int, line.split()))
        row = [int(x) for x in line.split()]
        matrix.append(row)
    # print(matrix)
    return matrix


def sumAboveDiagonals(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return (0, 0)

    sumAboveMainDiagonal = 0
    sumAboveSecondaryDiagonal = 0

    for i in range(n):
        for j in range(i + 1, n):
            sumAboveMainDiagonal += matrix[i][j]
        for j in range(n - i - 1):
            sumAboveSecondaryDiagonal += matrix[i][j]

    return (sumAboveMainDiagonal, sumAboveSecondaryDiagonal)

if __name__ == "__main__":
    filename = "matrix.txt"
    matrix = readMatrixFromFile(filename)
    print(sumAboveDiagonals(matrix))

