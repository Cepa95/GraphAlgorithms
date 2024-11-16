from readPajek import readPajek, convertToAdjList


def dfs(graph, node, visited):
    stack = [node]
    component = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            component.append(current)
            if current in graph:
                stack.extend(graph[current])
    return component


def findComponents(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = dfs(graph, node, visited)
            components.append(component)
    return components


def sizeOfLargestComponent(components):
    return max(len(component) for component in components)


def countEdges(graph, component):
    edgeCount = 0
    for node in component:
        if node in graph:
            edgeCount += len(graph[node])
    return edgeCount


def main():
    filename = "football.net"

    vertices, edges, isDirected = readPajek(filename)
    graph = convertToAdjList(vertices, edges, isDirected)

    components = findComponents(graph)
    numComponents = len(components)
    largestComponent = sizeOfLargestComponent(components)

    print(f"Number of components: {numComponents}")
    print(f"Size of the largest component: {largestComponent}")
    print("\nFirst ten components and their edge counts:")
    for component in components[:10]:
        edgeCount = countEdges(graph, component)
        print(f"Component {component[0]}: Size = {len(component)}, Edges = {edgeCount}")


if __name__ == "__main__":
    main()
