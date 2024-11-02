from exercise01 import readMatrixFromFile


def createDictionary(matrix):
    dictionary = {}
    for element in matrix:
        dictionary[element[0]] = element[1]
    return dictionary


if __name__ == "__main__":
    filename = "twoNum.txt"
    matrix = readMatrixFromFile(filename)
    print(matrix)

dictionary = createDictionary(matrix)
print(type(dictionary))
print(dictionary)
