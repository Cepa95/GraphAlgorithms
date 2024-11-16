from readPajek import readPajek, convertToAdjList


def primAlgorithm(adjList):
    startVertex = list(adjList.keys())[0]
    visited = set([startVertex])
    # print(f'adjList[startVertex]: {adjList[startVertex]}')
    edges = [
        (startVertex, neighbor, weight) for neighbor, weight in adjList[startVertex]
    ]
    # print(edges)
    mst = []

    while edges:
        minEdge = min(edges, key=lambda x: x[2])
        # print(f'minEdge: {minEdge}')
        # print(f'Edges: {edges}')
        edges.remove(minEdge)
        u, v, weight = minEdge

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, edgeWeight in adjList[v]:
                # print(adjList[v])
                if neighbor not in visited:
                    edges.append((v, neighbor, edgeWeight))
    return mst


def main():
    # filename = "airports-split.net"
    filename = "provjera.net"

    vertices, edges, directed = readPajek(filename)
    # print(f"vertices: {vertices}, edges: {edges}, directed: {directed}")
    adjList = convertToAdjList(vertices, edges, directed)
    print("Adjacency List:", adjList)

    mst = primAlgorithm(adjList)

    print("\nMinimum Spanning Tree (Prim's Algorithm):")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")





if __name__ == "__main__":
    main()
