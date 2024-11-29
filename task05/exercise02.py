from readPajek import readPajek, convertToAdjList


def bfs(start, graph):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            neighbors = graph.get(vertex, [])
        
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited


def findComponents(vertices, edges):
    graph = convertToAdjList(vertices, edges, True)
    #print(graph)
    visited = set()
    components = []

    for vertex in vertices:
        if vertex not in visited:
            component = bfs(vertex, graph)
            components.append(component)
            visited.update(component)

    return components


def findBiggestCompanies(vertices, edges):
    graph = convertToAdjList(vertices, edges, True)
    countOwnedCompanies = {}

    for company in vertices:
        ownedCompanies = bfs(company, graph)
        countOwnedCompanies[company] = len(ownedCompanies) - 1

    sortOwnedCompanies = list(countOwnedCompanies.items())
    sortOwnedCompanies.sort(key=lambda x: x[1], reverse=True)

    return sortOwnedCompanies[:10]


def main():
    filename = "eva.net"
    vertices, edges, isDirected = readPajek(filename)

    print(f"Total number of companies (vertices): {len(vertices)}")
    print(f"Total number of ownership relations (edges): {len(edges)}")

    components = findComponents(vertices, edges)
    numCompanies = len(components)
    largestComponentSize = max(len(component) for component in components)

    print(f"Number of components: {numCompanies}")
    print(f"Size of largest component: {largestComponentSize}")

    # Distribution of component sizes
    componentSize = [len(component) for component in components]

    componentSize.sort(reverse=True)
    print(f"Distribution of component sizes: {componentSize[:10]}")

    # Number of isolated nodes
    isolatedNodes = sum(1 for size in componentSize if size == 1)
    print(f"Number of isolated nodes: {isolatedNodes}")

    biggestCompanies = findBiggestCompanies(vertices, edges)
    print("Top 10 companies and the number of companies they own:")

    for company, count in biggestCompanies:
        print(f"Company {vertices[company]} owns {count} companies")


if __name__ == "__main__":
    main()
