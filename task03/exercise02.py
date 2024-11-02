from exercise01 import readMatrixFromFile


def sumMatrixRows(matrix):
    listSum = []

    for row in matrix:
        counter = 0
        for element in row:
            counter += element
        listSum.append(counter)
    return listSum


if __name__ == "__main__":
    filename = "matrix.txt"
    matrix = readMatrixFromFile(filename)
    # print(matrix)
    print(sumMatrixRows(matrix))
