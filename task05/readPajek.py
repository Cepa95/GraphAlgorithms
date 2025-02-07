def readPajek(filename):
    vertices = {}
    edges = []

    isDirected = False
    isReadingVertices = False
    isReadingArcs = False
    isReadingEdges = False

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith("*vertices"):
                isReadingVertices = True
                isReadingArcs = False
                isReadingEdges = False
                continue

            elif line.lower().startswith(("*arcs", "*edges")):
                isReadingVertices = False
                isReadingArcs = line.lower().startswith("*arcs")
                isReadingEdges = not isReadingArcs
                isDirected = isReadingArcs
                continue

            if isReadingVertices:
                parts = line.split()
                #print(parts)

                if len(parts) >= 2:
                    VerId = int(parts[0])

                    vertices[VerId] = parts[1]
                    #print(vertices[VerId])

            elif isReadingEdges or isReadingArcs:
                parts = line.split()
                if len(parts) >= 2:
                    u = int(parts[0])
                    v = int(parts[1])
                    if len(parts) >=3:
                        weight = int(parts[2])
                        edges.append((u, v, weight))
                    else:
                        edges.append((u, v))
    return vertices, edges, isDirected


def convertToAdjList(vertices, edges, directed):
    # adjList = {v: [] for v in vertices}
    adjList = {}
    for v in vertices:
        adjList[v] = []
    for edge in edges:
        if len(edge) == 3:
            u, v, weight = edge
            adjList[u].append((v, weight))
            if not directed:
                adjList[v].append((u, weight))
        else:
            u, v = edge
            adjList[u].append((v))
            if not directed:
                adjList[v].append((u))
            
    return adjList