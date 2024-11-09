def readPajekFile(filename):
    file = open(filename, "r")

    vertices = []
    edges = []
    isEdge = False

    for line in file:
        if line.startswith("*Vertices"):
            continue
        elif line.startswith("*Edges") or line.startswith("*Arcs"):
            isEdge = True
            continue
        if not isEdge:
            vertices.append(line.strip())
            # print(vertices)
        else:
            parts = line.strip().split()
            if len(parts) == 2:
                edges.append(tuple(map(int, parts)))
    return vertices, edges


def adjacencyMatrix(vertices, edges):
    n = len(vertices)
    # matrix = [[0] * n for _ in range(n)]
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)

        matrix.append(row)
    print(edges)
    for edge in edges:
        u, v = edge

        # print(u, v)
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = 1
    return matrix


def incidenceMatrix(vertices, edges):
    n = len(vertices)
    m = len(edges)

    # matrix = [[0] * m for _ in range(n)]
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    # print(edges)

    for i, edge in enumerate(edges):
        print(i, edge)
        u, v = edge

        matrix[u - 1][i] = 1
        matrix[v - 1][i] = 1
    return matrix


def adjacencyList(vertices, edges):
    adjList = {}
    for i in range(len(vertices)):
        adjList[i + 1] = []
    # print(adjList)

    for edge in edges:
        u, v = edge
        adjList[u].append(v)
        adjList[v].append(u)
    return adjList


def main():
    filename = "euler.net"

    vertices, edges = readPajekFile(filename)
    # adjMatrix = adjacencyMatrix(vertices, edges)
    # incMatrix = incidenceMatrix(vertices, edges)
    adjList = adjacencyList(vertices, edges)

    # print("Adjacency Matrix:")
    # for row in adjMatrix:
    #     print(row)
    # print("\nIncidence Matrix:")
    # for row in incMatrix:
    #     print(row)
    # print("\nAdjacency List:")
    for vertex, neighbors in adjList.items():
        print(f"{vertex}: {neighbors}")


if __name__ == "__main__":
    main()
