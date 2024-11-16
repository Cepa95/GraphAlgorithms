def readPajekFileAsAdjacencyList(filename):
    adjList = {}
    with open(filename, "r") as file:
        lines = file.readlines()
        verticesSection = False
        edgesSection = False

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("*Vertices"):
                verticesSection = True
                edgesSection = False
                continue
            elif line.startswith("*Edges") or line.startswith("*Arcs"):
                verticesSection = False
                edgesSection = True
                continue

            if verticesSection:
                parts = line.split()
                if len(parts) >= 1:
                    vertex_id = int(parts[0])
                    adjList[vertex_id] = []
            elif edgesSection:
                parts = line.split()
                if len(parts) >= 2:
                    u = int(parts[0])
                    v = int(parts[1])
                    adjList[u].append(v)
                    adjList[v].append(u)

    return adjList


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


def adjListToIncMatrix(adjList):
    vertices = list(adjList.keys())
    edges = []
    for vertex, neighbors in adjList.items():
        # print(neighbors)
        for neighbor in neighbors:
            if {vertex, neighbor} not in edges:
                edges.append({vertex, neighbor})

    incMatrix = []
    for i in range(len(vertices)):
        row = []
        for j in range(len(edges)):
            row.append(0)

        incMatrix.append(row)

    for edgeIndex, edge in enumerate(edges):
        vertex1, vertex2 = list(edge)
        vertex1Index = vertices.index(vertex1)
        vertex2Index = vertices.index(vertex2)
        incMatrix[vertex1Index][edgeIndex] = 1
        incMatrix[vertex2Index][edgeIndex] = 1

    return incMatrix


def adjListToAdjMatrix(adjList):
    vertices = list(adjList.keys())
    n = len(vertices)
    adjMatrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)

        adjMatrix.append(row)

    for vertex, neighbors in adjList.items():
        for neighbor in neighbors:
            # print(vertices)
            # print(vertices.index(3))
            # print(neighbors)
            vertexIndex = vertices.index(vertex)
            neighborIndex = vertices.index(neighbor)
            adjMatrix[vertexIndex][neighborIndex] = 1

    return adjMatrix


def main():
    filename = "euler.net"

    # vertices, edges = readPajekFile(filename)
    adjList = readPajekFileAsAdjacencyList(filename)
    print("\nAdjacency List:")
    for vertex, neighbors in adjList.items():
        print(f"{vertex}: {neighbors}")

    # adjMatrix = adjacencyMatrix(vertices, edges)
    # incMatrix = incidenceMatrix(vertices, edges)
    # adjList = adjacencyList(vertices, edges)
    # incMatrixFromAdjList = adjListToIncMatrix(adjList)
    # adjMatrixFromAdjList = adjListToAdjMatrix(adjList)
    # print(vertices, edges)

    # print("Adjacency Matrix:")
    # for row in adjMatrix:
    #     print(row)
    # print("\nIncidence Matrix:")
    # for row in incMatrix:
    #    print(row)
    # print("\nAdjacency List:")
    # for vertex, neighbors in adjList.items():
    #   print(f"{vertex}: {neighbors}")

    # print("\nIncidence Matrix:")
    # for row in incMatrixFromAdjList:
    #    print(row)

    # print("Adjacency Matrix:")
    # for row in  adjMatrixFromAdjList:
    #    print(row)


if __name__ == "__main__":
    main()
