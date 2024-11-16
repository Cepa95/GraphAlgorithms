from readPajek import readPajek, convertToAdjList


def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])  
        return parent[i]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def kruskalAlgorithm(vertices, edges):
    # parent = {v: v for v in vertices}
    # rank = {v: 0 for v in vertices}
    parent = {}
    for v in vertices:
        parent[v] = v
    #print(f'parent: {parent}')
    rank = {}
    for v in vertices:
        rank[v] = 0
    #print(f'rank: {rank}')

    #print(f"edges: {edges}")
    # Sort all the edges in non-decreasing order of their weight
    sortedEdges = sorted(edges, key=lambda x: x[2])
    #print(f'sortedEdges: {sortedEdges}')

    mst = []

    for edge in sortedEdges:
        u, v, weight = edge
        #print(find(parent, u))
        #print(parent)
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))

    return mst


def main():
    # filename = "airports-split.net"
    filename = "provjera.net"

    vertices, edges, directed = readPajek(filename)
    # print(f"vertices: {vertices}, edges: {edges}, directed: {directed}")
    #adjList = convertToAdjList(vertices, edges, directed)
    #print("Adjacency List:", adjList)

    mst = kruskalAlgorithm(vertices, edges)

    print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")


if __name__ == "__main__":
    main()
