from exercise01 import readMatrixFromFile


def checkMatrixColumns(matrix):
    numRows = len(matrix)
    numCols = max(len(row) for row in matrix)

    for i in range(numCols):
        counter = 0
        for j in range(numRows):
            if i < len(matrix[j]):
             
                if matrix[j][i] == 1:
                    counter += 1
                elif matrix[j][i] != 0:
                    return False

        if counter != 2:
            return False
    return True


if __name__ == "__main__":
    filename = "matrix1.txt"
    matrix = readMatrixFromFile(filename)
    print(matrix)

    print(checkMatrixColumns(matrix))
